from django.test import TestCase
from recipes.models import Unit, to_nearest_frac, to_frac_round_down, to_nearest_tsp

from django.core.urlresolvers import reverse

from model_mommy import mommy
from mock import Mock, patch

test_cases_nearest_tsp = (
                ((0.125), (0,1,8)),
                ((0.25), (0,1,4)),
                ((0.5), (0,1,2)),
                ((1), 1),
                ((1.1), (1,1,8)),
                ((2.2), (2,1,4)),
                ((3.3), (3,1,4)),
                ((4.4), (4,1,2)),
                ((5.5), (5,1,2)),
                ((6.6), (6,1,2)),
                ((7.7), (7,1,2)),
                ((8.8), 9),
                ((9.9), 10),
              )

class Utils(TestCase):
    def test_to_nearest_tsp(self):
            for x, expected_result in test_cases_nearest_tsp:
                self.assertEqual(expected_result, to_nearest_tsp(x))

class IngredientTest(TestCase):
    def setUp(self):
        self.mL = mommy.make('Unit', name='mL', name_abbrev='mL', type=Unit.TYPE.volume, system=Unit.SYSTEM.si)
        self.l = mommy.make('Unit', name='l', name_abbrev='l', type=Unit.TYPE.volume, system=Unit.SYSTEM.si)
        self.g = mommy.make('Unit', name='gram', name_abbrev='g', type=Unit.TYPE.mass, system=Unit.SYSTEM.si)
        self.kg = mommy.make('Unit', name='kilogram', name_abbrev='kg', type=Unit.TYPE.mass, system=Unit.SYSTEM.si)
        self.lb = mommy.make('Unit', name='pound', name_abbrev='lb', type=Unit.TYPE.mass, system=Unit.SYSTEM.imperial)
        self.cup = mommy.make('Unit', name='cup', name_abbrev='cup', type=Unit.TYPE.volume, system=Unit.SYSTEM.imperial)
        self.tbsp = mommy.make('Unit', name='tbsp', name_abbrev='tbsp', type=Unit.TYPE.volume, system=Unit.SYSTEM.imperial)
        self.tsp = mommy.make('Unit', name='tsp', name_abbrev='tsp', type=Unit.TYPE.volume, system=Unit.SYSTEM.imperial)
        self.floz = mommy.make('Unit', name='fluid_ounce', name_abbrev='floz', type=Unit.TYPE.volume, system=Unit.SYSTEM.imperial)

        self.egg = mommy.make('Food', name='egg', name_plural='eggs')
        self.bun = mommy.make('Food', name='bun', name_plural='buns', conversion_factor=50)
        self.ketchup = mommy.make('Food', name='ketchup')
        self.water = mommy.make('Food', name='water', conversion_src_unit=self.l, conversion_factor=1000)
        self.flour = mommy.make('Food', name='flour', conversion_src_unit=self.cup, conversion_factor=125)
        self.sugar = mommy.make('Food', name='sugar')
        self.tomatoes = mommy.make('Food', name='canned tomatoes')

        self.sifted = mommy.make('PrepMethod', name='sifted')

    def test_formatted_amount_no_unit(self):
        ingredient = mommy.make('Ingredient', amount=1.0, food=self.egg)
        self.assertEqual(ingredient._formatted_amount(1.),
                          "1")

    def test_formatted_amount_no_unit_range(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.egg)
        self.assertEqual(ingredient._formatted_amount(1),
                          "1 to 2")

    def test_formatted_food_plural_just1(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.egg)
        self.assertEqual(ingredient._formatted_food(),
                          "egg")

    def test_formatted_food_plural_2(self):
        ingredient = mommy.make('Ingredient', amount=2, food=self.egg)
        self.assertEqual(ingredient._formatted_food(),
                          "eggs")

    def test_formatted_food_plural_range1to2(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.egg)
        self.assertEqual(ingredient._formatted_food(),
                          "eggs")

    def test_formatted_amount_mL(self):
        ingredient = mommy.make('Ingredient', amount=100.0, food=self.ketchup, unit=self.mL)
        self.assertEqual(ingredient.formatted_amount(),
                          "100 mL ketchup")

    def test_formatted_amount_mL_range(self):
        ingredient = mommy.make('Ingredient', amount=100.0, amountMax=150, food=self.ketchup, unit=self.mL)
        self.assertEqual(ingredient.formatted_amount(),
                          "100 to 150 mL ketchup")

    def test_formatted_amount_mL(self):
        ingredient = mommy.make('Ingredient', amount=101.0, food=self.water, unit=self.mL)
        self.assertEqual(ingredient._formatted_amount(1.),
                          "101 mL")

    def test_formatted_grams_mL(self):
        ingredient = mommy.make('Ingredient', amount=101.0, food=self.water, unit=self.mL)
        self.assertEqual(ingredient._formatted_grams(1.),
                          "(101 g)")

    def test_formatted_amount_mL_range(self):
        ingredient = mommy.make('Ingredient', amount=101.0, amountMax=102, food=self.water, unit=self.mL)
        self.assertEqual(ingredient._formatted_amount(1.),
                          "101 to 102 mL")

    def test_formatted_grams_mL_range(self):
        ingredient = mommy.make('Ingredient', amount=101.0, amountMax=102, food=self.water, unit=self.mL)
        self.assertEqual(ingredient._formatted_grams(1.),
                          "(101 to 102 g)")


    def test_formatted_amount_g(self):
        ingredient = mommy.make('Ingredient', amount=100, food=self.water, unit=self.g)
        self.assertEqual(ingredient._formatted_amount(1),
                          "100 g")

    def test_formatted_amount_g_to_kg_range_nice1(self):
        ingredient = mommy.make('Ingredient', amount=900, amountMax=1100, food=self.water, unit=self.g)
        self.assertEqual(ingredient._formatted_amount(1),
                          "900 g to 1.1 kg")

    def test_formatted_amount_g_to_kg_range_nice2(self):
        ingredient = mommy.make('Ingredient', amount=900, amountMax=950, food=self.water, unit=self.g)
        self.assertEqual(ingredient._formatted_amount(1),
                          "900 to 950 g")

    def test_formatted_amount_g_to_kg_range_nice3(self):
        ingredient = mommy.make('Ingredient', amount=1.1, amountMax=1.2, food=self.water, unit=self.kg)
        self.assertEqual(ingredient._formatted_amount(1),
                          "1.1 to 1.2 kg")

    def test_formatted_grams_g_to_kg_range_nice3(self):
        ingredient = mommy.make('Ingredient', amount=1.1, amountMax=1.2, food=self.water, unit=self.kg)
        self.assertEqual(ingredient._formatted_grams(1),
                          "")

    def test_formatted_amount_g_to_kg_nice(self):
        ingredient = mommy.make('Ingredient', amount=3000, food=self.water, unit=self.g)
        self.assertEqual(ingredient._formatted_amount(1),
                          "3 kg")

    def test_formatted_amount_fluid_ounce(self):
        ingredient = mommy.make('Ingredient', amount=14, food=self.tomatoes, unit=self.floz)
        self.assertEqual(ingredient._formatted_amount(1),
                          "14 floz")

    def test_formatted_amount_lb_to_kg_nice(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_amount(1),
                          "1 lb")

    def test_formatted_grams_lb_to_kg_nice(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_grams(1),
                          "(454 g)")

    def test_formatted_amount_lb_to_kg_range_nice1(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_amount(1),
                          "1 to 2 lb")

#    def test_formatted_amount_lb_plural(self):
#        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.sugar, unit=self.lb)
#        self.assertEqual(ingredient._formatted_amount(1),
#                          "1 to 2 lbs")

    def test_formatted_grams_lb_to_kg_range_nice1(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_grams(1),
                          "(454 to 907 g)")

    def test_formatted_amount_lb_to_kg_range_nice2(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=3, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_amount(1.),
                          "1 to 3 lb")

    def test_formatted_grams_lb_to_kg_range_nice2(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=3, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_grams(1.),
                          "(454 g to 1.361 kg)")

    def test_formatted_amount_lb_to_kg_range_nice3(self):
        ingredient = mommy.make('Ingredient', amount=3, amountMax=4, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_amount(1.),
                          "3 to 4 lb")

    def test_formatted_grams_lb_to_kg_range_nice3(self):
        ingredient = mommy.make('Ingredient', amount=3, amountMax=4, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_grams(1.),
                          "(1.361 to 1.814 kg)")

    def test_formatted_amount_lb_to_kg_range_nice4(self):
        ingredient = mommy.make('Ingredient', amount=3.1, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_amount(1),
                          "3.1 lb")

    def test_formatted_grams_lb_to_kg_range_nice4(self):
        ingredient = mommy.make('Ingredient', amount=3.1, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_grams(1),
                          "(1.406 kg)")

    def test_formatted_amount_lb_to_kg_range_nice5(self):
        ingredient = mommy.make('Ingredient', amount=3.1, amountMax=3.2, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_amount(1.),
                          "3.1 to 3.2 lb")

    def test_formatted_grams_lb_to_kg_range_nice5(self):
        ingredient = mommy.make('Ingredient', amount=3.1, amountMax=3.2, food=self.sugar, unit=self.lb)
        self.assertEqual(ingredient._formatted_grams(1.),
                          "(1.406 to 1.451 kg)")

    def test_formatted_amount_cups_tbsp_nice1(self):
        ingredient = mommy.make('Ingredient', amount=1.083333333334, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1),
                          "1 cup, 1 Tbsp, 1 tsp")

    def test_formatted_grams_cups_tbsp_nice1(self):
        ingredient = mommy.make('Ingredient', amount=1.083333333334, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_grams(1),
                          "(135 g)")

    def test_formatted_amount_cups_tbsp_nice2(self):
        ingredient = mommy.make('Ingredient', amount=1.083333333333, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1),
                          "1 cup, 1 Tbsp, 1 tsp")

    def test_formatted_grams_cups_tbsp_nice2(self):
        ingredient = mommy.make('Ingredient', amount=1.083333333333, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_grams(1),
                          "(135 g)")

    def test_formatted_amount_cups_fractions(self):
        ingredient = mommy.make('Ingredient', amount=1.5, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1),
                          "1 <sup>1</sup>&frasl;<sub>2</sub> cup")

    def test_formatted_grams_cups_fractions(self):
        ingredient = mommy.make('Ingredient', amount=1.5, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_grams(1),
                          "(188 g)")

    def test_formatted_amount_cups_fractions_quarts1(self):
        ingredient = mommy.make('Ingredient', amount=9, food=self.sugar, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1),
                          "2 quarts, 1 cup")

    def test_formatted_amount_cups_fractions_quarts2(self):
        ingredient = mommy.make('Ingredient', amount=4.5, food=self.sugar, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1),
                          "4 <sup>1</sup>&frasl;<sub>2</sub> cups")

    def test_formatted_amount_cups_fractions_quarts3(self):
        ingredient = mommy.make('Ingredient', amount=7.5, food=self.sugar, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1),
                          "7 <sup>1</sup>&frasl;<sub>2</sub> cups")

    def test_formatted_amount_cups_fractions_special_case1(self):
        ingredient = mommy.make('Ingredient', amount=0.3334, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1),
                          "<sup>1</sup>&frasl;<sub>3</sub> cup")

    def test_formatted_grams_cups_fractions_special_case1(self):
        ingredient = mommy.make('Ingredient', amount=0.3334, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_grams(1),
                          "(42 g)")

    def test_formatted_amount_cups_fractions_special_case2(self):
        ingredient = mommy.make('Ingredient', amount=0.33333333333, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1),
                          "<sup>1</sup>&frasl;<sub>3</sub> cup")

    def test_formatted_grams_cups_fractions_special_case2(self):
        ingredient = mommy.make('Ingredient', amount=0.33333333333, food=self.flour, unit=self.cup)
        self.assertEqual(ingredient._formatted_grams(1),
                          "(42 g)")

    def test_formatted_amount_cups_fractions_special_case3(self):
        ingredient = mommy.make('Ingredient', amount=0.25, food=self.sugar, unit=self.tsp)
        self.assertEqual(ingredient._formatted_amount(1),
                          "<sup>1</sup>&frasl;<sub>4</sub> tsp")

    def test_formatted_amount_cups_plural(self):
        ingredient = mommy.make('Ingredient', amount=2, food=self.sugar, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1),
                          "2 cups")

    def test_formatted_amount_tsp(self):
        ingredient = mommy.make('Ingredient', amount=0.3333333333333333333, food=self.sugar, unit=self.tsp)
        self.assertEqual(ingredient._formatted_amount(1.),
                          "<sup>1</sup>&frasl;<sub>4</sub> tsp")

    def test_formatted_amount_unitless(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.bun)
        self.assertEqual(ingredient._formatted_amount(1.),
                          "1")

    def test_formatted_grams_unitless_with_conversion(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.bun)
        self.assertEqual(ingredient._formatted_grams(1.),
                          "(50 g)")

    def test_formatted_grams_range_unitless_with_conversion(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.bun)
        self.assertEqual(ingredient._formatted_grams(1.),
                          "(50 to 100 g)")

    def test_prep_method_None(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.cup)
        self.assertEqual(ingredient._formatted_prep(),
                          "")

    def test_prep_method(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.cup, prep_method=self.sifted)
        self.assertEqual(ingredient._formatted_prep(),
                          ", sifted")

    def test_formatted_amount_dont_show_decimal(self):
        tartshells = mommy.make('Food', name='3" tart shells')
        ingredient = mommy.make('Ingredient', amount=12.0, food=tartshells, unit=None)
        self.assertEqual(ingredient._formatted_amount(1.),
                          '12')

    def test_formatted_amount_scale(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(scale=2),
                          '2 cups')

    def test_formatted_amount_scale_max(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.sugar, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(scale=2),
                          '2 to 4 cups')

    def test_formatted_amount_range_cups(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.sugar, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1.),
                          '1 to 2 cups')

    def test_formatted_amount_range_mixed_imperial(self):
        ingredient = mommy.make('Ingredient', amount=0.0625, amountMax=2, food=self.sugar, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(1.),
                          '1 Tbsp to 2 cups')

    def test_formatted_amount_5Tbsp(self):
        ingredient = mommy.make('Ingredient', amount=5, food=self.sugar, unit=self.tbsp)
        self.assertEqual(ingredient._formatted_amount(1.),
                          '5 Tbsp')

    def test_formatted_amount_pinch(self):
        ingredient = mommy.make('Ingredient', amount=0.05, unit=self.tsp)
        self.assertEqual(ingredient._formatted_amount(1.), 'pinch of')

    def test_formatted_amount_eight_tsp(self):
        ingredient = mommy.make('Ingredient', amount=0.125, unit=self.tsp)
        self.assertEqual(ingredient._formatted_amount(1.), '<sup>1</sup>&frasl;<sub>8</sub> tsp')

    def test_formatted_amount_null_amount(self):
        ingredient = mommy.make('Ingredient', food=self.sugar)
        self.assertEqual(ingredient._formatted_amount(1.), '')

    def test_formatted_grams_null_amount(self):
        ingredient = mommy.make('Ingredient', food=self.sugar)
        self.assertEqual(ingredient._formatted_grams(1.), '')

    def test_floats(self):
        ingredient = mommy.make('Ingredient', food=self.sugar, amount=0.6666666666666666666, unit=self.cup)
        self.assertEqual(ingredient._formatted_amount(2.), '1 <sup>1</sup>&frasl;<sub>3</sub> cup')


test_cases_nearest = {tuple(range(1,5)): (
                ((0.1), 0),
                ((0.2), (0,1,4)),
                ((0.3), (0,1,3)),
                ((0.4), (0,1,3)),
                ((0.5), (0,1,2)),
                ((0.6), (0,2,3)),
                ((0.7), (0,2,3)),
                ((0.8), (0,3,4)),
                ((0.9), 1),
                ((1.0), 1),
              )}

test_cases_round_down = {4: (
                ((0.1), 0),
                ((0.2), 0),
                ((0.3), (0,1,4,0.05)),
                ((0.4), (0,1,3,0.0667)),
                ((0.5), (0,1,2,0)),
                ((0.6), (0,1,2,0.1)),
                ((0.7), (0,2,3,0.0333)),
                ((0.8), (0,3,4,0.05)),
                ((0.9), (0,3,4,0.15)),
                ((1.0), 1),
              )}


class TestFractions(TestCase):
    def test_to_nearest_frac(self):
        for maxdenom, x_and_expected in test_cases_nearest.iteritems():
            for x, expected in x_and_expected:
                result = to_nearest_frac(x, maxdenom)
                self.assertEqual(result, expected)

    def test_to_frac_round_down(self):
        for maxdenom, x_and_expected in test_cases_round_down.iteritems():
            for x, expected in x_and_expected:
                result = to_frac_round_down(x, maxdenom)
                self.assertEqual(result, expected)

class SourceTest(TestCase):
    def test_unicode(self):
        s = mommy.make('Source')
        self.assertEqual(unicode(s), s.name)

class CategoryTest(TestCase):
    def test_unicode(self):
        c = mommy.make('Category')
        self.assertEqual(unicode(c), c.name)

class FoodGroupTest(TestCase):
    def test_unicode(self):
        f = mommy.make('FoodGroup')
        self.assertEqual(unicode(f), f.name)

class PrepMethodTest(TestCase):
    def test_unicode(self):
        p = mommy.make('PrepMethod')
        self.assertEqual(unicode(p), p.name)

class RecipeTest(TestCase):
    def test_unicode(self):
        r = mommy.make('Recipe')
        self.assertEqual(unicode(r), r.title)

    def test_get_serving_None(self):
        r = mommy.make('Recipe')
        self.assertEqual(r.get_serving(), None)

    def test_get_serving(self):
        serving_string = mommy.make('ServingString', text='serves %s')
        r = mommy.make('Recipe', serving_value=2, serving_string=serving_string)
        self.assertEqual(r.get_serving(), 'serves 2')

    def test_get_serving_serving_value_None(self):
        serving_string = mommy.make('ServingString', text='serves %s')
        r = mommy.make('Recipe', serving_string=serving_string)
        self.assertEqual(r.get_serving(), None)

    def test_get_serving_serving_string_None(self):
        r = mommy.make('Recipe', serving_value=2)
        self.assertEqual(r.get_serving(), None)

    def test_get_serving_serving_string_text_blank(self):
        serving_string = mommy.make('ServingString', text='')
        r = mommy.make('Recipe', serving_value=2, serving_string=serving_string)
        self.assertEqual(r.get_serving(), None)

    def test_get_serving_serving_string_text_blank(self):
        serving_string = mommy.make('ServingString', text='blah blah')
        r = mommy.make('Recipe', serving_value=2, serving_string=serving_string)
        self.assertEqual(r.get_serving(), None)

    def test_get_text(self):
        p = mommy.make('PrepMethod', name='chopped')
        r = mommy.make('Recipe')
        f = mommy.make('Food', name='food', conversion_factor=125, detail='detail')
        d1 = mommy.make('Direction', text='dir 1', recipe=r)
        d2 = mommy.make('Direction', text='dir 2', recipe=r)
        i1 = mommy.make('Ingredient', amount='1', food=f, recipe=r, direction=d1)
        i2 = mommy.make('Ingredient', amount='1', food=f, recipe=r, direction=d1)
        i3 = mommy.make('Ingredient', amount='1', food=f, recipe=r, direction=d2)
        i4 = mommy.make('Ingredient', amount='1', food=f, recipe=r, direction=d2, prep_method=p)

        ret = r.get_text()
        expected = [(u'dir 1', [('1', '(125 g)', u'food', '', u'detail'), ('1', '(125 g)', u'food', '', u'detail')]), (u'dir 2', [('1', '(125 g)', u'food', '', u'detail'), ('1', '(125 g)', u'food', u', chopped', u'detail')])]
        self.assertEqual(ret, expected)

class UnitTest(TestCase):
    def test_unicode(self):
        u = mommy.make('Unit')
        self.assertEqual(unicode(u), u.name)

class FoodTest(TestCase):
    def test_unicode(self):
        f = mommy.make('Food')
        self.assertEqual(unicode(f), f.name_sorted)

    def test_get_grams_same_unit(self):
        cups = mommy.make('Unit', name='cups')
        f = mommy.make('Food', conversion_src_unit=cups, conversion_factor=125.)
        cup_grams = f.get_grams_in_cup()
        self.assertEqual(cup_grams, '125 g')

    def test_get_grams_different_unit1(self):
        cups = mommy.make('Unit', name='cups')
        f = mommy.make('Food', conversion_src_unit=cups, conversion_factor=125.)
        tbsp_grams = f.get_grams_in_tbsp()
        self.assertEqual(tbsp_grams, '8 g')

    def test_get_grams_different_unit2(self):
        cups = mommy.make('Unit', name='cups')
        f = mommy.make('Food', conversion_src_unit=cups, conversion_factor=125.)
        tsp_grams = f.get_grams_in_tsp()
        self.assertEqual(tsp_grams, '3 g')

    def test_get_grams_different_unit3(self):
        cups = mommy.make('Unit', name='cups')
        f = mommy.make('Food', conversion_src_unit=cups, conversion_factor=125.)
        mL_grams = f.get_grams_in_100mL()
        self.assertEqual(mL_grams, '53 g')

    def test_get_grams_for_unit(self):
        f = mommy.make('Food', conversion_factor=125.)
        grams = f.get_grams_for_unit()
        self.assertEqual(grams, '125 g')


class DirectionTest(TestCase):
    def test_unicode_title_too_long(self):
        d = mommy.make('Direction', text='abcdefghijklmnopqrstuvwxyzabcdefghijklmno')
        self.assertEqual(unicode(d), 'abcdefghijklmnopqrstuvwxyzabcdefghijklmn...')

    def test_unicode_just_right(self):
        d = mommy.make('Direction', text='abcdefghijklmnopqrstuvwxyzabcdefghijklmn')
        self.assertEqual(unicode(d), 'abcdefghijklmnopqrstuvwxyzabcdefghijklmn')

    def test_unicode_short(self):
        d = mommy.make('Direction', text='a')
        self.assertEqual(unicode(d), 'a')
