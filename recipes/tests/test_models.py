from django.test import TestCase
from recipes.models import Unit, to_nearest_frac, to_frac_round_down, to_nearest_tsp

from django.core.urlresolvers import reverse

from model_mommy import mommy
from mock import Mock, patch

class RecipeTest(TestCase):
    def test(self):
        cat = mommy.make('Recipe', title="title")

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
                self.assertEquals(expected_result, to_nearest_tsp(x))

class IngredientTest(TestCase):
    def setUp(self):
        self.mL = mommy.make('Unit', name='mL', name_abbrev='mL', type=Unit.TYPE.volume, system=Unit.SYSTEM.si)
        self.l = mommy.make('Unit', name='l', name_abbrev='l', type=Unit.TYPE.volume, system=Unit.SYSTEM.si)
        self.g = mommy.make('Unit', name='gram', name_abbrev='g', type=Unit.TYPE.mass, system=Unit.SYSTEM.si)
        self.kg = mommy.make('Unit', name='kilogram', name_abbrev='kg', type=Unit.TYPE.mass, system=Unit.SYSTEM.si)
        self.lb = mommy.make('Unit', name='pound', name_abbrev='lb', type=Unit.TYPE.mass, system=Unit.SYSTEM.imperial)
        self.cup = mommy.make('Unit', name='cup', name_abbrev='cup', type=Unit.TYPE.volume, system=Unit.SYSTEM.imperial)
        self.tsp = mommy.make('Unit', name='tsp', name_abbrev='tsp', type=Unit.TYPE.volume, system=Unit.SYSTEM.imperial)
        self.floz = mommy.make('Unit', name='fluid_ounce', name_abbrev='floz', type=Unit.TYPE.volume, system=Unit.SYSTEM.imperial)

        self.egg = mommy.make('Food', name='egg', name_plural='eggs')
        self.ketchup = mommy.make('Food', name='ketchup')
        self.water = mommy.make('Food', name='water', conversion_src_unit=self.l, conversion_factor=1000)
        self.flour = mommy.make('Food', name='flour', conversion_src_unit=self.cup, conversion_factor=125)
        self.sugar = mommy.make('Food', name='sugar')
        self.tomatoes = mommy.make('Food', name='canned tomatoes')


        self.sifted = mommy.make('PrepMethod', name='sifted')

    def test_formatted_amount_no_unit(self):
        ingredient = mommy.make('Ingredient', amount=1.0, food=self.egg)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 egg")

    def test_formatted_amount_no_unit_plural(self):
        ingredient = mommy.make('Ingredient', amount=2, food=self.egg)
        self.assertEquals(ingredient.formatted_amount(),
                          "2 eggs")

    def test_formatted_amount_no_unit_range(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.egg)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 to 2 eggs")

    def test_formatted_amount_mL(self):
        ingredient = mommy.make('Ingredient', amount=100.0, food=self.ketchup, unit=self.mL)
        self.assertEquals(ingredient.formatted_amount(),
                          "100 mL ketchup")

    def test_formatted_amount_mL_range(self):
        ingredient = mommy.make('Ingredient', amount=100.0, amountMax=150, food=self.ketchup, unit=self.mL)
        self.assertEquals(ingredient.formatted_amount(),
                          "100 to 150 mL ketchup")

    def test_formatted_amount_mL_grams_conversion(self):
        ingredient = mommy.make('Ingredient', amount=101.0, food=self.water, unit=self.mL)
        self.assertEquals(ingredient.formatted_amount(),
                          "101 mL (101 g) water")

    def test_formatted_amount_mL_range_grams_conversion(self):
        ingredient = mommy.make('Ingredient', amount=101.0, amountMax=102, food=self.water, unit=self.mL)
        self.assertEquals(ingredient.formatted_amount(),
                          "101 to 102 mL (101 to 102 g) water")

    def test_formatted_amount_g(self):
        ingredient = mommy.make('Ingredient', amount=100, food=self.water, unit=self.g)
        self.assertEquals(ingredient.formatted_amount(),
                          "100 g water")

    def test_formatted_amount_g_to_kg_range_nice1(self):
        ingredient = mommy.make('Ingredient', amount=900, amountMax=1100, food=self.water, unit=self.g)
        self.assertEquals(ingredient.formatted_amount(),
                          "900 g to 1.1 kg water")

    def test_formatted_amount_g_to_kg_range_nice2(self):
        ingredient = mommy.make('Ingredient', amount=900, amountMax=950, food=self.water, unit=self.g)
        self.assertEquals(ingredient.formatted_amount(),
                          "900 to 950 g water")

    def test_formatted_amount_g_to_kg_range_nice3(self):
        ingredient = mommy.make('Ingredient', amount=1.1, amountMax=1.2, food=self.water, unit=self.kg)
        self.assertEquals(ingredient.formatted_amount(),
                          "1.1 to 1.2 kg water")

    def test_formatted_amount_g_to_kg_nice(self):
        ingredient = mommy.make('Ingredient', amount=3000, food=self.water, unit=self.g)
        self.assertEquals(ingredient.formatted_amount(),
                          "3 kg water")

    def test_formatted_amount_fluid_ounce(self):
        ingredient = mommy.make('Ingredient', amount=14, food=self.tomatoes, unit=self.floz)
        self.assertEquals(ingredient.formatted_amount(),
                          "14 floz canned tomatoes")

    def test_formatted_amount_lb_to_kg_nice(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.lb)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 lb (454 g) sugar")

    def test_formatted_amount_lb_to_kg_range_nice1(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=2, food=self.sugar, unit=self.lb)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 to 2 lb (454 to 907 g) sugar")

    def test_formatted_amount_lb_to_kg_range_nice2(self):
        ingredient = mommy.make('Ingredient', amount=1, amountMax=3, food=self.sugar, unit=self.lb)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 to 3 lb (454 g to 1.361 kg) sugar")

    def test_formatted_amount_lb_to_kg_range_nice3(self):
        ingredient = mommy.make('Ingredient', amount=3, amountMax=4, food=self.sugar, unit=self.lb)
        self.assertEquals(ingredient.formatted_amount(),
                          "3 to 4 lb (1.361 to 1.814 kg) sugar")

    def test_formatted_amount_lb_to_kg_range_nice4(self):
        ingredient = mommy.make('Ingredient', amount=3.1, food=self.sugar, unit=self.lb)
        self.assertEquals(ingredient.formatted_amount(),
                          "3.1 lb (1.406 kg) sugar")

    def test_formatted_amount_lb_to_kg_range_nice5(self):
        ingredient = mommy.make('Ingredient', amount=3.1, amountMax=3.2, food=self.sugar, unit=self.lb)
        self.assertEquals(ingredient.formatted_amount(),
                          "3.1 to 3.2 lb (1.406 to 1.451 kg) sugar")

    def test_formatted_amount_cups_tbsp_nice1(self):
        ingredient = mommy.make('Ingredient', amount=1.083333333334, food=self.flour, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 cup, 1 Tbsp, 1 tsp (135 g) flour")

    def test_formatted_amount_cups_tbsp_nice2(self):
        ingredient = mommy.make('Ingredient', amount=1.083333333333, food=self.flour, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 cup, 1 Tbsp, 1 tsp (135 g) flour")

    def test_formatted_amount_cups_fractions(self):
        ingredient = mommy.make('Ingredient', amount=1.5, food=self.flour, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 1/2 cup (188 g) flour")

    def test_formatted_amount_cups_fractions_special_case(self):
        ingredient = mommy.make('Ingredient', amount=4.5, food=self.sugar, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 quart, 1/2 cup sugar")

    def test_formatted_amount_cups_fractions_special_case1(self):
        ingredient = mommy.make('Ingredient', amount=0.3334, food=self.flour, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1/3 cup (42 g) flour")

    def test_formatted_amount_cups_fractions_special_case2(self):
        ingredient = mommy.make('Ingredient', amount=0.33333333333, food=self.flour, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1/3 cup (42 g) flour")

    def test_formatted_amount_cups_fractions_special_case3(self):
        ingredient = mommy.make('Ingredient', amount=0.25, food=self.sugar, unit=self.tsp)
        self.assertEquals(ingredient.formatted_amount(),
                          "1/4 tsp sugar")

    def test_formatted_amount_cups_plural(self):
        ingredient = mommy.make('Ingredient', amount=2, food=self.sugar, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "2 cups sugar")

    def test_formatted_amount_tsp(self):
        ingredient = mommy.make('Ingredient', amount=0.3333333333333333333, food=self.sugar, unit=self.tsp)
        self.assertEquals(ingredient.formatted_amount(),
                          "1/4 tsp sugar")

    def test_formatted_amount_prep_method(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.cup, prep_method=self.sifted)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 cup sifted sugar")

    def test_formatted_amount_instruction(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.cup, instruction='fried')
        self.assertEquals(ingredient.formatted_amount(),
                          "1 cup sugar (fried)")

    def test_formatted_amount_tar_shells(self):
        tartshells = mommy.make('Food', name='3" tart shells')
        ingredient = mommy.make('Ingredient', amount=12.0, food=tartshells, unit=None)
        self.assertEquals(ingredient.formatted_amount(),
                          '12 3" tart shells')

    def test_unicode(self):
        i = mommy.make('Ingredient', amount=1.1, amountMax=2.1, food=self.sugar, unit=self.cup, prep_method=self.sifted, instruction='fried')
        self.assertEquals(unicode(i), i.formatted_amount())

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
                self.assertEquals(result, expected)

    def test_to_frac_round_down(self):
        for maxdenom, x_and_expected in test_cases_round_down.iteritems():
            for x, expected in x_and_expected:
                result = to_frac_round_down(x, maxdenom)
                self.assertEquals(result, expected)

class SourceTest(TestCase):
    def test_unicode(self):
        s = mommy.make('Source')
        self.assertEquals(unicode(s), s.name)

class CategoryTest(TestCase):
    def test_unicode(self):
        c = mommy.make('Category')
        self.assertEquals(unicode(c), c.name)

class FoodGroupTest(TestCase):
    def test_unicode(self):
        f = mommy.make('FoodGroup')
        self.assertEquals(unicode(f), f.name)

class PrepMethodTest(TestCase):
    def test_unicode(self):
        p = mommy.make('PrepMethod')
        self.assertEquals(unicode(p), p.name)

class RecipeTest(TestCase):
    def test_unicode(self):
        r = mommy.make('Recipe')
        self.assertEquals(unicode(r), r.title)

class UnitTest(TestCase):
    def test_unicode(self):
        u = mommy.make('Unit')
        self.assertEquals(unicode(u), u.name)

class FoodTest(TestCase):
    def test_unicode(self):
        f = mommy.make('Food')
        self.assertEquals(unicode(f), f.name_sorted)

class DirectionTest(TestCase):
    def test_unicode_title_too_long(self):
        d = mommy.make('Direction', text='abcdefghijklmnopqrstuvwxyzabcdefghijklmno')
        self.assertEquals(unicode(d), 'abcdefghijklmnopqrstuvwxyzabcdefghijklmn...')

    def test_unicode_just_right(self):
        d = mommy.make('Direction', text='abcdefghijklmnopqrstuvwxyzabcdefghijklmn')
        self.assertEquals(unicode(d), 'abcdefghijklmnopqrstuvwxyzabcdefghijklmn')

    def test_unicode_short(self):
        d = mommy.make('Direction', text='a')
        self.assertEquals(unicode(d), 'a')
