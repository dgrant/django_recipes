from django.db import models
import datetime
from positions.fields import PositionField
from model_utils import Choices
from .templatetags.fractions import text_fraction
import math

def nice_float(x):
    sig_figs = 3
#    ret = round(x, -int(math.floor(math.log10(x))) + (sig_figs - 1))
    ret = round(x)
    ret = "{0}".format(ret)
    while (ret.find('.') != -1 and ret[-1] == '0') or ret[-1] == '.':
        ret = ret[:-1]
    return ret


class Source(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField(max_length=500, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, help_text="Maximum 120 characters")
    order_index = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(unique=True, help_text="Automatically generated from the title")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ["order_index"]

    def get_absolute_url(self):
        return "/cookbook/categories/%s/" % self.slug

class FoodGroup(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class PrepMethod(models.Model):
    name = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return self.name

    def save(self):
        self.name = self.name.lower()
        super(PrepMethod, self).save()

    class Meta:
        ordering = ["-name"]

class Photo(models.Model):
    caption = models.CharField(max_length=200)
    recipe = models.ForeignKey('Recipe')
    image = models.ImageField(upload_to='images')
    #This field used because can't make ImageField core right now (see http://code.djangoproject.com/ticket/2534)
    keep = models.BooleanField(default=True, editable=False)

    def __unicode__(self):
        return str(self.recipe) + ' (%s)' % self.image

    def save(self):
        # Don't save if there is no image (since core field is always set).
        if not self.id and not self.image:
            return
        super(Photo, self).save()

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=50, null=False, blank=False)
    prep_time = models.CharField(max_length=100, blank=True) # This field type is a guess.
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    sources = models.ManyToManyField(Source, blank=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def save(self):
        self.mtime = datetime.datetime.now()
        super(Recipe, self).save()

    @models.permalink
    def get_absolute_url(self):
        '''This is just used from the admin interface'''
        return ('recipe_detail_by_slug', [self.slug])

class DirectionManager(models.Manager):

    def all(self):
        return self.prefetch_related('ingredients', 'ingredients__unit', 'ingredients__food', 'ingredients__prep_method', 'ingredients__food__conversion_src_unit')

class Direction(models.Model):
    """
    A direction is a step in a recipe's preparation and each recipe can have
    multiple directions but obviously, each direction only applies to one
    recipe.
    """
    text = models.TextField(blank=True)
    recipe = models.ForeignKey(Recipe, related_name='directions')
    order = PositionField(blank=True, null=True, unique_for_field='recipe')

    objects = DirectionManager()

    def __unicode__(self):
        ret = self.text[:40]
        if len(self.text) > 40:
            ret += "..."
        return ret

    class Meta:
        ordering = ['order', 'id']

class Unit(models.Model):
    name = models.CharField(max_length=60, unique=True)
    name_abbrev = models.CharField(max_length=60, blank=True)
    plural = models.CharField(max_length=60, blank=True)
    plural_abbrev = models.CharField(max_length=60, blank=True)
    TYPE = Choices((0, 'other', 'Other'), (1, 'mass', 'Mass'), (2, 'volume', 'Volume'))
    type = models.IntegerField(choices=TYPE)
    SYSTEM = Choices((0, 'si', 'SI'), (1, 'imperial', 'Imperial'))
    system = models.IntegerField(choices=SYSTEM, null=True)

    def __unicode__(self):
        return self.plural

    class Meta:
        ordering = ["name"]

class Food(models.Model):
    name = models.CharField(max_length=150)
    name_sorted = models.CharField(max_length=150, default='')
    group = models.ForeignKey(FoodGroup)
    conversion_src_unit = models.ForeignKey(Unit, related_name='+', null=True, blank=True)
    conversion_factor = models.FloatField(null=True, blank=True)
    name_plural = models.CharField(max_length=150, null=True, blank=True)

    def __unicode__(self):
        return self.name_sorted

    class Meta:
        ordering = ["name_sorted",]

class UnitConversion(models.Model):
    from_unit = models.ForeignKey(Unit, related_name='conversions_from')
    to_unit = models.ForeignKey(Unit, related_name='conversions_to')
    multiplier = models.FloatField()

    def save(self):
        if self.from_unit.type == self.to_unit.type:
            super(UnitConversion, self).save()
        else:
            print "types don't match"

    class Meta:
        unique_together = (('from_unit', 'to_unit'))

class Ingredient(models.Model):
    amount = models.FloatField()
    amountMax = models.FloatField(null=True, blank=True)
    unit = models.ForeignKey(Unit, null=True, blank=True)
    recipe = models.ForeignKey(Recipe)
    food = models.ForeignKey(Food)
    prep_method = models.ForeignKey(PrepMethod, null=True, blank=True)
    instruction = models.CharField(max_length=50, blank=True, default='')
    order_index = PositionField(blank=True, null=True, unique_for_field="direction")
    direction = models.ForeignKey(Direction, blank=True, null=True, related_name='ingredients')

    def __init__(self, *args, **kwargs):
        super(Ingredient, self).__init__(*args, **kwargs)

    def combined_amount(self):
        if self.unit is None:
            if self.amountMax is None:
                ret = "{0}".format(nice_float(self.amount))
            else:
                ret = "{0}-{1}".format(nice_float(self.amount), nice_float(self.amountMax))

        elif self.unit.system is None or self.unit.type == Unit.TYPE.other or self.food.conversion_src_unit is None:
            if self.amountMax is None:
                ret = "{0} {1}".format(text_fraction(self.amount), self.unit.plural_abbrev)
            else:
                ret = "{0}-{1} {2}".format(text_fraction(self.amount), text_fraction(self.amountMax), self.unit.plural_abbrev)

        # Case 1: ingredient is in imperial volume (ie. cups, Tbsp.)
        # Original is "1 cup"
        elif self.unit.system == Unit.SYSTEM.imperial and self.unit.type == Unit.TYPE.volume:
            converted_amount = self.amount
            # First, get it into the src unit for the Food conversion
            if self.unit.pk != self.food.conversion_src_unit.pk:
                unit_converter = UnitConversion.objects.get(from_unit=self.unit, to_unit=self.food.conversion_src_unit)
                converted_amount = converted_amount * unit_converter.multiplier
            # Then convert to grams
            converted_amount = converted_amount * self.food.conversion_factor

            if self.amountMax is None:
                ret = "{0} {1} ({2} {3})".format(text_fraction(self.amount), self.unit.plural_abbrev, nice_float(converted_amount), 'g')
            else:
                converted_maxAmount = self.amountMax * self.food.conversion_factor * unit_converter.multiplier
                ret = "{0}-{1} {2} ({3}-{4} {5})".format(text_fraction(self.amount), text_fraction(self.amountMax), self.unit.plural_abbrev, nice_float(converted_amount), nice_float(converted_maxAmount), 'g')

        # Case 2: ingredient is in imperial weight (ie. lbs)
        # Original is "1 lb"

        # Case 3: ingredient is in metric volume (ie. mL)
        # Original is "50 mL" -> "50 mL (61 g)"

        # Case 4: ingredient is in metric weight (ie. kg) or ingredient has "other" type or "null" system

        if self.prep_method != None:
            ret += " " + self.prep_method.name
        if self.food.name_plural != None and self.food.name_plural != '' and self.amount != 1:
            ret += " " + self.food.name_plural
        else:
            ret += " " + self.food.name
        if self.instruction != None and self.instruction != '':
            ret += " (" + self.instruction + ")"

        return ret

    def __unicode__(self):
        if self.amount == int(self.amount):
            amount = str(int(self.amount))
        else:
            amount = self.amount
        if self.amount == 1 and self.amountMax is None:
            if self.unit != None:
                unit = str(self.unit.name)
            else:
                unit = ''
        else:
            if self.unit != None:
                unit = self.unit.plural
            else:
                unit = ''
        food = str(self.food).lower()
        return "%s %s %s" % (amount, unit, food)

    class Meta:
        ordering = ["direction", "order_index", "id"]

