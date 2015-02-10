from django.db import models
import datetime
from positions.fields import PositionField
from model_utils import Choices
import math
from django.utils.translation import ugettext_lazy as _

from pint import UnitRegistry

ureg = UnitRegistry()


def to_nearest_frac(x, denoms):
    """
    Convert x to a common fraction.

    Chooses the closest fraction to x with denominator <= maxdenom.
    If x is closest to an integer, return that integer; otherwise,
    return an (integer, numerator, denominator) tuple.
    """

    assert x >= 0, "_to_frac only works on positive numbers."

    intpart = int(x)
    x -= intpart

    bestfrac = 0, 1
    mindiff = x

    for denom in denoms:
        # for each denominator, there are two numerators to consider:
        # the one below x and the one above x
        for num in (int(x * denom), int(x * denom + 1)):
            diff = abs(x - float(num) / denom)

            # compare using '<' rather than '<=' to ensure that the
            # fraction with the smallest denominator is preferred
            if diff < mindiff:
                bestfrac = num, denom
                mindiff = diff

    if bestfrac[0] == 0:
        return intpart
    elif mindiff >= 1 - x:
        return intpart + 1
    else:
        return intpart, bestfrac[0], bestfrac[1]


def to_frac_round_down(x, maxdenom):
    """
    Convert x to a common fraction.

    Chooses the closest fraction to x with denominator <= maxdenom.
    If x is closest to an integer, return that integer; otherwise,
    return an (integer, numerator, denominator) tuple.
    """

    assert x >= 0, "_to_frac only works on positive numbers."
    orig_x = x
    intpart = int(x)
    x -= intpart

    bestfrac = 0, 1
    mindiff = x
    for denom in range(1, maxdenom + 1):
        # for each denominator, there are two numerators to consider:
        # the one below x and the one above x
        num = int(x * denom + 0.001)
        diff = x - float(num) / denom

        # compare using '<' rather than '<=' to ensure that the
        # fraction with the smallest denominator is preferred
        if diff < mindiff:
            bestfrac = num, denom
            mindiff = diff

    if bestfrac[0] == 0:
        return intpart
    else:
        remainder = orig_x - (intpart + float(bestfrac[0]) / float(bestfrac[1]))
        return intpart, bestfrac[0], bestfrac[1], round(remainder, 4)


def nice_grams(x):
    """ x is a Pint quantity in cups """
    kg = x.to(ureg.kg)
    if kg.magnitude < 1:
        return nice_float(x.magnitude) + " g"
    else:
        return nice_float(kg.magnitude, sig_figs=4) + " kg"


def nice_grams_range(x, y):
    assert x <= y
    x_kg = x.to(ureg.kg)
    y_kg = y.to(ureg.kg)
    if x_kg.magnitude < 1 and y_kg.magnitude < 1:
        return "{0} to {1} g".format(nice_float(x.magnitude), nice_float(y.magnitude))
    elif x_kg.magnitude < 1 and y_kg.magnitude >= 1:
        return "{0} g to {1} kg".format(nice_float(x.magnitude), nice_float(y_kg.magnitude, sig_figs=4))
    else:
        # x_kg.magnitude >= 1 and y_kg.magnitude >= 1:
        return "{0} to {1} kg".format(nice_float(x_kg.magnitude, sig_figs=4), nice_float(y_kg.magnitude, sig_figs=4))


def to_nearest_tsp(x):
    intpart = int(x)
    x -= intpart
    assert x <= 1
    num_dens = ((0, 1), (1, 8), (1, 4), (1, 2), (1, 1))
    bestDiff = 2
    for num, den in num_dens:
        diff = abs(float(num) / float(den) - x)
        if diff < bestDiff:
            best = num, den
            bestDiff = diff
    if best[0] == 0:
        return intpart
    elif bestDiff >= 1 - x:
        return intpart + 1
    else:
        return intpart, best[0], best[1]


def format_unit(int_part, unit_str, num=None, den=None):
    ret = ''
    if int_part != '':
        ret += int_part + ' '
    if num != None and den != None:
        ret += '<sup>' + num + '</sup>' + '&frasl;' + '<sub>' + den + '</sub> '
    ret += unit_str
    ret += ', '
    return ret


def nice_cups(x):
    """ x is a Pint object (quantity) in cups """
    tsp = x.to(ureg.teaspoon)
    tsp = round(tsp.magnitude, 4) * ureg.teaspoon

    # Special cases
    if tsp.magnitude == 15:
        return '5 Tbsp'

    units = ((ureg.quarts, ('quart', 'quarts')), (ureg.cups, ('cup', 'cups')), (ureg.tablespoons, ('Tbsp', 'Tbsp')),
             (ureg.teaspoons, 'tsp'))
    leftover = tsp
    ret = ''
    for unit, unit_strs in units:
        how_many_unit = leftover.to(unit)
        how_many_int = int(how_many_unit.magnitude)
        if how_many_int != 0 or unit == ureg.teaspoons or unit == ureg.cups:
            if unit == ureg.cups:
                # Cups need to be formatted as a mixed fraction, using a maximum denominator of 4.
                result = to_frac_round_down(how_many_unit.magnitude, maxdenom=4)
                if type(result) == tuple:
                    how_many_int, num, den, rem = result
                    int_str = '' if how_many_int == 0 else str(how_many_int)
                    ret += format_unit(int_str, unit_strs[0] if how_many_int <= 1 else unit_strs[1], str(num), str(den))
                    leftover = rem * unit
                else:
                    how_many_int = result
                    if how_many_int != 0:
                        ret += format_unit(str(how_many_int), unit_strs[0] if how_many_int <= 1 else unit_strs[1])
                    leftover = (round(how_many_unit.magnitude, 4) - how_many_int) * unit
            elif unit == ureg.teaspoons:
                # Teaspoons need some special care, they need to be formated as 1/8, 1/4, 1/2 but nothing else.
                result = to_nearest_tsp(how_many_unit.magnitude)
                if type(result) == tuple:
                    how_many_int, num, den = result
                    int_str = '' if how_many_int == 0 else str(how_many_int)
                    ret += format_unit(int_str, unit_strs, str(num), str(den))
                    leftover = (round(how_many_unit.magnitude, 4) - how_many_int - round(float(num) / float(den),
                                                                                         4)) * unit
                else:
                    how_many_int = result
                    if how_many_int != 0:
                        ret += format_unit(str(how_many_int), unit_strs)
                    leftover = (round(how_many_unit.magnitude, 4) - how_many_int) * unit
            elif unit == ureg.quarts and how_many_int == 1:
                # if we only have 1 quart, doing display and quarts... just use 4+ cups instead
                leftover = how_many_unit
            else:
                # Tablespoons and quarts and everything else bigger than that: don't do any fractions for these.
                ret += format_unit(str(how_many_int), unit_strs[0] if how_many_int <= 1 else unit_strs[1])
                leftover = (round(how_many_unit.magnitude, 4) - how_many_int) * unit
        else:
            leftover = how_many_unit
    if ret != '':
        while ret[-1] == ',' or ret[-1] == ' ':
            ret = ret[:-1]
    else:
        ret = 'pinch of'
    return ret


def nice_cups_range(cups, maxCups):
    start = nice_cups(cups)
    start_units = start.split(' ')[-1]
    end = nice_cups(maxCups)
    end_units = end.split(' ')[-1]
    min_len = min(len(start_units), len(end_units))
    if start_units[:min_len - 1] == end_units[:min_len - 1]:
        return ' '.join(start.split(' ')[:-1]) + ' to ' + end
    else:
        return start + ' to ' + end


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
    name = models.CharField(max_length=150, verbose_name=_('Source|name'))
    url = models.URLField(max_length=500, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')
        ordering = ["name"]


class Category(models.Model):
    name = models.CharField(max_length=120,
                            unique=True,
                            help_text="Maximum 120 characters",
                            verbose_name=_('Category|name'))
    slug = models.SlugField(unique=True, help_text='Automatically generated from the title')
    order_index = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['order_index']


class FoodGroup(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('FoodGroup|name'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('FoodGroup')
        verbose_name_plural = _('FoodGroups')
        ordering = ['name']


class PrepMethod(models.Model):
    name = models.CharField(max_length=60, blank=True, verbose_name=_('PrepMethod|name'))

    def __unicode__(self):
        return self.name

    def save(self):
        self.name = self.name.lower()
        super(PrepMethod, self).save()

    class Meta:
        verbose_name = _('Preparation Method')
        verbose_name_plural = _('Preparation Methods')
        ordering = ['-name']


class Photo(models.Model):
    caption = models.CharField(max_length=200, verbose_name=_('Photo|caption'))
    recipe = models.ForeignKey('Recipe')
    image = models.ImageField(upload_to='images')
    # This field used because can't make ImageField core right now (see http://code.djangoproject.com/ticket/2534)
    keep = models.BooleanField(default=True, editable=False)

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')


# def save(self):
# Don't save if there is no image (since core field is always set).


# if not self.id and not self.image:
# return
#        super(Photo, self).save()

class ServingString(models.Model):
    text = models.CharField(max_length=50, verbose_name=_('ServingString|text'))

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = _('Serving String')
        verbose_name_plural = _('Serving Strings')


class Recipe(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Recipe|title'))
    summary = models.CharField(max_length=500, blank=True, verbose_name=_('Recipe|summary'))
    description = models.TextField(blank=True, verbose_name=_('Recipe|description'))
    slug = models.SlugField(unique=True, max_length=50, null=False, blank=False)
    prep_time = models.CharField(max_length=100, blank=True)  # This field type is a guess.
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    sources = models.ManyToManyField(Source, blank=True)
    category = models.ForeignKey(Category)
    serving_string = models.ForeignKey(ServingString, null=True, blank=True)
    serving_value = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _('Recipe')
        verbose_name_plural = _('Recipies')

    def save(self):
        self.mtime = datetime.datetime.now()
        self.scale = 1.0
        super(Recipe, self).save()

    def get_text(self):
        a = []
        for direction in self.directions.all():
            ingredients = []
            for ingredient in direction.ingredients.all():
                ingredients.append((ingredient._formatted_amount(self.scale),
                                    ingredient._formatted_grams(self.scale),
                                    ingredient._formatted_food(),
                                    ingredient._formatted_prep(),
                                    ingredient.food.detail))
            a.append((direction.text, ingredients))
        return a

    def get_serving(self):
        if self.serving_value != None != '' and self.serving_string != None and self.serving_string.text != '' and self.serving_string.text.find(
                '%s') != -1:
            num_sig_figs = len(str(self.serving_value))
            serving_value_scaled = nice_float(self.serving_value * self.scale, num_sig_figs)
            return self.serving_string.text % (serving_value_scaled,)
        else:
            return None


class DirectionManager(models.Manager):
    def all(self):
        return self.prefetch_related('ingredients', 'ingredients__unit', 'ingredients__food',
                                     'ingredients__prep_method', 'ingredients__food__conversion_src_unit')


class Direction(models.Model):
    """
    A direction is a step in a recipe's preparation and each recipe can have
    multiple directions but obviously, each direction only applies to one
    recipe.
    """
    text = models.TextField(blank=True, verbose_name=_('Direction|text'))
    recipe = models.ForeignKey(Recipe, related_name='directions')
    order = PositionField(blank=True, null=True, unique_for_field='recipe')

    objects = DirectionManager()

    def __unicode__(self):
        ret = self.text[:40]
        if len(self.text) > 40:
            ret += "..."
        return ret

    class Meta:
        verbose_name = _('Direction')
        verbose_name_plural = _('Directions')
        ordering = ['order', 'id']


class Unit(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name=_('Unit|name'))
    name_abbrev = models.CharField(max_length=60, blank=True, verbose_name=_('Unit|name_abbrev'))
    plural_abbrev = models.CharField(max_length=60, blank=True, verbose_name=_('Unit|plural_abbrev'))
    TYPE = Choices((0, 'other', 'Other'), (1, 'mass', 'Mass'), (2, 'volume', 'Volume'))
    type = models.IntegerField(choices=TYPE)
    SYSTEM = Choices((0, 'si', 'SI'), (1, 'imperial', 'Imperial'))
    system = models.IntegerField(choices=SYSTEM, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')
        ordering = ["name"]


class FoodManager(models.Manager):
    def with_conversions(self):
        return self.prefetch_related('conversion_src_unit').filter(conversion_factor__isnull=False)


class Food(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Food|name'))
    name_sorted = models.CharField(max_length=150, default='', verbose_name=_('Food|name_sorted'))
    group = models.ForeignKey(FoodGroup)
    conversion_src_unit = models.ForeignKey(Unit, related_name='+', null=True, blank=True)
    conversion_factor = models.FloatField(null=True, blank=True)
    name_plural = models.CharField(max_length=150, null=True, blank=True)
    detail = models.TextField(blank=True)

    objects = FoodManager()

    def __unicode__(self):
        return self.name_sorted

    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Foods')
        ordering = ["name_sorted", ]

    def get_grams(self, amount_u):
        conversion_factor_u = self.conversion_factor * (ureg.grams / ureg[self.conversion_src_unit.name])
        conversion_factor_u = conversion_factor_u.to(ureg.grams / amount_u)
        return nice_grams(conversion_factor_u * amount_u)

    def get_grams_in_cup(self):
        return self.get_grams(ureg.cup)

    def get_grams_in_tbsp(self):
        return self.get_grams(ureg.tbsp)

    def get_grams_in_tsp(self):
        return self.get_grams(ureg.tsp)

    def get_grams_in_100mL(self):
        return self.get_grams(100 * ureg.ml)

    def get_grams_for_unit(self):
        return nice_grams(self.conversion_factor * ureg.grams)

    def has_unitless_conversion(self):
        return self.conversion_src_unit == None and self.conversion_factor != None

    def has_imperial_conversion(self):
        return self.conversion_src_unit != None and self.conversion_src_unit.name in (
            'millilitre', 'cup', 'tablespoon', 'teaspoon') and self.conversion_factor != None


class Ingredient(models.Model):
    amount = models.FloatField(null=True, blank=True, verbose_name=_('Ingredient|amount'))
    amountMax = models.FloatField(null=True, blank=True)
    unit = models.ForeignKey(Unit, null=True, blank=True)
    recipe = models.ForeignKey(Recipe)
    food = models.ForeignKey(Food)
    prep_method = models.ForeignKey(PrepMethod, null=True, blank=True)
    order_index = PositionField(blank=True, null=True, unique_for_field="direction")
    direction = models.ForeignKey(Direction, related_name='ingredients', null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super(Ingredient, self).__init__(*args, **kwargs)

    def _formatted_food(self):
        if self.food.name_plural != None and self.food.name_plural != '' and (
                        self.amount != 1 or self.amountMax != None):
            food_str = self.food.name_plural
        else:
            food_str = self.food.name
        return food_str

    def _formatted_prep(self):
        prep_method_str = ''
        if self.prep_method != None:
            prep_method_str = ', ' + self.prep_method.name
        return prep_method_str

    def _formatted_amount(self, scale):
        if self.amount == None:
            return ''

        amount = self.amount * scale
        if self.amountMax != None:
            amountMax = self.amountMax * scale
        else:
            amountMax = None

        unit_str = ''
        amountStr = ''
        amountMax_str = ''
        if self.unit != None and self.unit.type == Unit.TYPE.mass and self.unit.system == Unit.SYSTEM.si:
            # grams, kilograms
            amount_g = (amount * ureg[self.unit.name]).to(ureg.grams)
            if amountMax == None:
                amount_str = '{0}'.format(nice_grams(amount_g))
            else:
                amountMax_g = (amountMax * ureg[self.unit.name]).to(ureg.grams)
                amount_str = '{0}'.format(nice_grams_range(amount_g, amountMax_g))

        elif self.unit != None and self.unit.type == Unit.TYPE.volume and self.unit.system == Unit.SYSTEM.imperial \
                and ureg[self.unit.name] in [ureg.quarts, ureg.cups, ureg.tablespoons, ureg.teaspoons]:
            # tsp, tbsp, cups, quarts
            amount_cups = (amount * ureg[self.unit.name]).to(ureg.cups)
            if amountMax != None:
                amountMax_cups = (amountMax * ureg[self.unit.name]).to(ureg.cups)
                amount_str = nice_cups_range(amount_cups, amountMax_cups)
            else:
                amount_str = nice_cups(amount_cups)

        else:
            # everything else
            amount_str = '{0}'.format(nice_float(amount, sig_figs=4))

            if amountMax != None:
                amountMax_str = ' to {0}'.format(nice_float(amountMax, sig_figs=4))

            if self.unit != None:
                unit_str = ' {0}'.format(self.unit.name_abbrev)

        return amount_str + amountMax_str + unit_str

    def _formatted_grams(self, scale):
        if self.amount == None:
            return ''

        amount = self.amount * scale
        if self.amountMax != None:
            amountMax = self.amountMax * scale
        else:
            amountMax = None

        grams_str = ''
        amount_g = None
        # This translates the following to grams, 1) any volumes that have conversions defined
        # 2) any imperial mass
        if self.unit != None and ( \
                    (
                                        self.unit.type == Unit.TYPE.volume and self.food.conversion_src_unit != None and self.food.conversion_factor != None) or \
                        (self.unit.type == Unit.TYPE.mass and self.unit.system == Unit.SYSTEM.imperial)):
            amount_u = amount * ureg[self.unit.name]
            if amountMax != None:
                amountMax_u = amountMax * ureg[self.unit.name]

            if self.food.conversion_src_unit != None and self.food.conversion_factor != None and self.unit.type != Unit.TYPE.mass:
                # First, get it into the src unit for the Food conversion, if necessary
                if self.unit.pk != self.food.conversion_src_unit.pk:
                    src_unit = ureg[self.food.conversion_src_unit.name]
                    amount_u = amount_u.to(src_unit)
                    if amountMax != None:
                        amountMax_u = amountMax_u.to(src_unit)
                # Then convert to grams
                conversion_factor = (self.food.conversion_factor * ureg.grams) / (
                    1.0 * ureg[self.food.conversion_src_unit.name])
                amount_g = conversion_factor * amount_u
                if amountMax != None:
                    amountMax_g = conversion_factor * amountMax_u
            else:
                amount_g = amount_u.to(ureg.grams)
                if amountMax != None:
                    amountMax_g = amountMax_u.to(ureg.grams)

        elif self.unit == None and self.food.conversion_factor != None and self.food.conversion_src_unit == None:
            amount_g = ureg.grams * self.food.conversion_factor * amount
            if amountMax != None:
                amountMax_g = ureg.grams * self.food.conversion_factor * amountMax

        if amount_g != None:
            if amountMax == None:
                grams_str = '({0})'.format(nice_grams(amount_g))
            else:
                grams_str = '({0})'.format(nice_grams_range(amount_g, amountMax_g))

        return grams_str

    class Meta:
        ordering = ["direction", "order_index", "id"]
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')

