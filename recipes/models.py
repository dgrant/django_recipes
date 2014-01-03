from django.db import models
import datetime
from positions.fields import PositionField
from model_utils import Choices
from .templatetags.fractions import text_fraction
import math

from pint import UnitRegistry
ureg = UnitRegistry()

def to_nearest_frac(x, maxdenom):
    """
    Convert x to a common fraction.

    Chooses the closest fraction to x with denominator <= maxdenom.
    If x is closest to an integer, return that integer; otherwise,
    return an (integer, numerator, denominator) tuple.
    """

    assert x >= 0, "_to_frac only works on positive numbers."

    intpart = int(x)
    x -= intpart

    bestfrac = 0,1
    mindiff = x

    for denom in range(1, maxdenom+1):
        # for each denominator, there are two numerators to consider:
        # the one below x and the one above x
        for num in (int(x*denom), int(x*denom+1)):
            diff = abs(x - float(num)/denom)

            # compare using '<' rather than '<=' to ensure that the
            # fraction with the smallest denominator is preferred
            if diff < mindiff:
                bestfrac = num, denom
                mindiff = diff

    if bestfrac[0] == 0:
        return intpart
    elif mindiff >= 1-x:
        return intpart+1
    else:
        return intpart, bestfrac[0], bestfrac[1]

def to_frac_round_down(x, maxdenom=10):
    """
    Convert x to a common fraction.

    Chooses the closest fraction to x with denominator <= maxdenom.
    If x is closest to an integer, return that integer; otherwise,
    return an (integer, numerator, denominator) tuple.
    """

    assert x >= 0, "_to_frac only works on positive numbers."

    intpart = int(x)
    x -= intpart

    bestfrac = 0,1
    mindiff = x

    for denom in range(1, maxdenom+1):
        # for each denominator, there are two numerators to consider:
        # the one below x and the one above x
        for num in [int(x*denom)]:
            num = int(x*denom)
            diff = x - float(num)/denom

            # compare using '<' rather than '<=' to ensure that the
            # fraction with the smallest denominator is preferred
            if diff < mindiff:
                bestfrac = num, denom
                mindiff = diff

    if bestfrac[0] == 0:
        return intpart
    else:
        return intpart, bestfrac[0], bestfrac[1]

def nice_grams(x):
    ''' x is a Pint quantity in cups '''
    kg = x.to(ureg.kg)
    if kg.magnitude < 1:
        return nice_float(x.magnitude) + " g"
    else:
        return nice_float(kg.magnitude, sig_figs=4) + " kg"

def nice_cups(x):
    ''' x is a Pint quantity in cups '''
    tsp = x.to(ureg.teaspoon)
    units = ((ureg.quarts, 'quart'), (ureg.cups, 'cup'), (ureg.tablespoons, 'Tbsp'), (ureg.teaspoons, 'tsp'))
    leftover = tsp
    ret = ''
    for unit, unit_str in units:
        how_many_unit = leftover.to(unit)
        how_many_int = int(how_many_unit.magnitude)
        leftover = (how_many_unit.magnitude - how_many_int) * unit
        if how_many_int != 0:
            ret += '{0} {1}, '.format(how_many_int, unit_str)
    while ret[-1] == ',' or ret[-1] == ' ':
        ret = ret[:-1]
    return ret

def nice_grams_range(x, y):
    x_kg = x.to(ureg.kg)
    y_kg = y.to(ureg.kg)
    if x_kg.magnitude < 1 and y_kg.magnitude < 1:
        return "{0} to {1} g".format(nice_float(x.magnitude), nice_float(y.magnitude))
    elif x_kg.magnitude < 1 and y_kg.magnitude >= 1:
        return "{0} g to {1} kg".format(nice_float(x.magnitude), nice_float(y_kg.magnitude, sig_figs=4))
    elif x_kg.magnitude >= 1 and y_kg.magnitude >= 1:
        return "{0} to {1} kg".format(nice_float(x_kg.magnitude, sig_figs=4), nice_float(y_kg.magnitude, sig_figs=4))
    else:
        raise Exception("Should never get here!")


def nice_float(x, sig_figs=None):
    if sig_figs is None:
        ret = round(x)
    else:
        ret = round(x, -int(math.floor(math.log10(x))) + (sig_figs - 1))
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
    plural_abbrev = models.CharField(max_length=60, blank=True)
    TYPE = Choices((0, 'other', 'Other'), (1, 'mass', 'Mass'), (2, 'volume', 'Volume'))
    type = models.IntegerField(choices=TYPE)
    SYSTEM = Choices((0, 'si', 'SI'), (1, 'imperial', 'Imperial'))
    system = models.IntegerField(choices=SYSTEM, null=True)

    def __unicode__(self):
        return self.name

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

    def formatted_amount(self):
        unit_str = ''
        amountMax_str = ''
        if self.unit != None and self.unit.type == Unit.TYPE.mass and self.unit.system == Unit.SYSTEM.si:
            # grams, kilograms
            amount_g = (self.amount * ureg[self.unit.name]).to(ureg.grams)
            amount_str = '{0}'.format(nice_grams(amount_g))
        elif self.unit != None and self.unit.type == Unit.TYPE.volume and self.unit.system == Unit.SYSTEM.imperial:
            amount_cups = (self.amount * ureg[self.unit.name]).to(ureg.cups)
            amount_str = nice_cups(amount_cups)
        else:
            # everything else
            amount_str = '{0}'.format(nice_float(self.amount, sig_figs=4))

            if self.amountMax != None:
                amountMax_str = ' to {0}'.format(nice_float(self.amountMax))

            if self.unit != None:
                unit_str = ' {0}'.format(self.unit.name_abbrev)

        grams_str = ''
        if self.unit != None and self.unit.type != Unit.TYPE.mass and self.food.conversion_src_unit != None and self.food.conversion_factor != None:
            amount_u = self.amount * ureg[self.unit.name]
            if self.amountMax != None:
                amountMax_u = self.amountMax * ureg[self.unit.name]
            # First, get it into the src unit for the Food conversion, if necessary
            if self.unit.pk != self.food.conversion_src_unit.pk:
                src_unit = ureg[self.food.conversion_src_unit.name]
                amount_u = amount_u.to(src_unit)
                if self.amountMax != None:
                    amountMax_u = amountMax_u.to(src_unit)
            # Then convert to grams
            conversion_factor = (self.food.conversion_factor * ureg.grams) / (1.0 * ureg[self.food.conversion_src_unit.name])
            amount_g = conversion_factor * amount_u
            if self.amountMax != None:
                amountMax_g = conversion_factor * amountMax_u

            if self.amountMax == None:
                grams_str = ' ({0})'.format(nice_grams(amount_g))
            else:
                grams_str = ' ({0})'.format(nice_grams_range(amount_g, amountMax_g))

        if self.food.name_plural != None and (self.amount != 1 or self.amountMax != None):
            food_str = self.food.name_plural
        else:
            food_str = self.food.name

        return '{0}{1}{2}{3} {4}'.format(amount_str, amountMax_str, unit_str, grams_str, food_str)

    def formatted_amount_old(self):
        # Case 1: things like eggs, tart shells, onion. No units. eg. "1 onion" or "1 egg"
        if self.unit == None:
            if self.amountMax == None:
                ret = "{0}".format(nice_float(self.amount))
            else:
                ret = "{0}-{1}".format(nice_float(self.amount), nice_float(self.amountMax))


        # Case 3: ingredient is in imperial volume
        # Original is "1 cup"
        elif (self.unit.system == Unit.SYSTEM.imperial or self.unit.system == Unit.SYSTEM.si) and self.unit.type == Unit.TYPE.volume and self.food.conversion_src_unit is not None:
            amount_u = self.amount * ureg[self.unit.name]
            if self.amountMax is not None:
                amountMax_u = self.amountMax * ureg[self.unit.name]
            # First, get it into the src unit for the Food conversion
            if self.unit.pk != self.food.conversion_src_unit.pk:
                src_unit = ureg[self.food.conversion_src_unit.name]
                amount_u = amount_u.to(src_unit)
                if self.amountMax is not None:
                    amountMax_u = amountMax_u.to(src_unit)
            # Then convert to grams
            conversion_factor = (self.food.conversion_factor * ureg.grams) / (1.0 * ureg[self.food.conversion_src_unit.name])
            amount_g = conversion_factor * amount_u
            if self.amountMax is not None:
                amountMax_g = conversion_factor * amountMax_u

            if self.amountMax is None:
                ret = "{0} {1} ({2})".format(text_fraction(self.amount), self.unit.plural_abbrev, nice_grams(amount_g))
            else:
                ret = "{0} to {1} {2} ({3})".format(text_fraction(self.amount), text_fraction(self.amountMax), self.unit.plural_abbrev, nice_grams_range(amount_g, amountMax_g))

        # Case 4: ingredient is in imperial weight (ie. lbs)
        # Original is "1 lb"
        elif self.unit.system == Unit.SYSTEM.imperial and self.unit.type == Unit.TYPE.mass:
            amount_u = self.amount * ureg[self.unit.name]
            amount_g = amount_u.to(ureg.grams)
            if self.amountMax is None:
                ret = "{0} {1} ({2})".format(nice_float(nice_float(self.amount, sig_figs=3), self.unit.plural_abbrev, nice_grams(amount_g)))
            else:
                amountMax_u = self.amountMax * ureg[self.unit.name]
                amountMax_g = amountMax_u.to(ureg.grams)
                ret = "{0} to {1} {2} ({3})".format(nice_float(self.amount, sig_figs=3), nice_float(self.amountMax, sig_figs=3), self.unit.plural_abbrev, nice_grams_range(amount_g, amountMax_g))


        # Case 2: things with a unit like "clove", "slice", "squirt". eg. "3 clove garlic" or "2 slices watermelon"
        #         for now this also includes things with no grams conversion, just print it out. This may fall to other cases below later.
        elif self.unit.system is None or self.unit.type == Unit.TYPE.other or self.food.conversion_src_unit is None:
            ret = text_fraction(self.amount)
            if self.amountMax is not None:
                ret += "-" + text_fraction(self.amountMax)
            ret += " " + self.unit.plural_abbrev

        else:
            raise Exception("Should not get here!")

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
                unit = self.unit.name
            else:
                unit = ''
        food = str(self.food).lower()
        return "%s %s %s" % (amount, unit, food)

    class Meta:
        ordering = ["direction", "order_index", "id"]

