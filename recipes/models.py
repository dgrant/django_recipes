from django.db import models
from tagging.fields import TagField
import datetime
from positions.fields import PositionField

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

class Food(models.Model):
    name = models.CharField(max_length=150)
    group = models.ForeignKey(FoodGroup)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name", "group"]

class PrepMethod(models.Model):
    name = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return self.name

    def save(self):
        self.name = self.name.lower()
        super(PrepMethod, self).save()

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

    tags = TagField()

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

class Direction(models.Model):
    """
    A direction is a step in a recipe's preparation and each recipe can have
    multiple directions but obviously, each direction only applies to one
    recipe.
    """
    text = models.TextField(blank=True)
    recipe = models.ForeignKey(Recipe)
    order = PositionField(blank=True, null=True, unique_for_field='recipe')

    def __unicode__(self):
        ret = self.text[:40]
        if len(self.text) > 40:
            ret += "..."
        return ret

    class Meta:
        ordering = ['order', 'id']

class Unit(models.Model):
    name = models.CharField(max_length=60)
    name_abbrev = models.CharField(max_length=60, blank=True)
    plural = models.CharField(max_length=60, blank=True)
    plural_abbrev = models.CharField(max_length=60, blank=True)
    type = models.IntegerField(choices=((0, 'Other'),(1, 'Mass'),(2, 'Volume')))

    def __unicode__(self):
        return self.plural

    class Meta:
        ordering = ["name"]

class Ingredient(models.Model):
    """
    TODO: move this lower later to get rid of quotes in ForeignKey references
    """
    amount = models.FloatField()
    amountMax = models.FloatField(null=True, blank=True)
    unit = models.ForeignKey(Unit,null=True, blank=True)
    recipe = models.ForeignKey(Recipe)
    food = models.ForeignKey(Food)
    prep_method = models.ForeignKey(PrepMethod, null=True, blank=True)
    order_index = PositionField(blank=True, null=True, unique_for_field="direction")
    direction = models.ForeignKey(Direction, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super(Ingredient, self).__init__(*args, **kwargs)

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

#class RatingCriteria(models.Model):
#    id = models.IntegerField(primary_key=True)
#    name = models.TextField(blank=True)
#    class Meta:
#        db_table = u'rating_criteria'

#class RatingCriterionList(models.Model):
#    rating_id = models.IntegerField()
#    rating_criterion_id = models.IntegerField(null=True, blank=True)
#    stars = models.FloatField(null=True, blank=True)
#    class Meta:
#        db_table = u'rating_criterion_list'

#class Ratings(models.Model):
#    id = models.IntegerField(primary_key=True)
#    recipe_id = models.IntegerField()
#    comment = models.TextField(blank=True)
#    rater = models.TextField(blank=True)
#    created = models.DateTimeField()
#    class Meta:
#        db_table = u'ratings'

#Things like 5 cal/g for certain ingredients
#class IngredientInfo(models.Model):
#    ingredient_id = models.ManyToManyField(Ingredient)
#    property_id = models.ManyToManyField(IngredientProperty)
#    amount = models.FloatField(null=True, blank=True)
#    per_units = models.ManyToManyField(Unit)
#    class Meta:
#        db_table = u'ingredient_info'



#Properties like cal/g or grams of fat/g
#class IngredientProperty(models.Model):
#    id = models.IntegerField(primary_key=True)
#    name = models.CharField(max_length=60, blank=True)
#    units = models.CharField(max_length=60, blank=True)
#    class Meta:
#        db_table = u'ingredient_properties'

#class IngredientWeights(models.Model):
#    id = models.IntegerField(primary_key=True)
#    ingredient_id = models.IntegerField()
#    amount = models.FloatField(null=True, blank=True)
#    unit_id = models.IntegerField(null=True, blank=True)
#    weight = models.FloatField(null=True, blank=True)
#    weight_unit_id = models.IntegerField(null=True, blank=True)
#    prep_method_id = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = u'ingredient_weights'

