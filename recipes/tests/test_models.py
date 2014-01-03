from django.test import TestCase
from recipes.models import Unit, to_nearest_frac, to_frac_round_down

from django.core.urlresolvers import reverse

from model_mommy import mommy
from mock import Mock, patch

class RecipeTest(TestCase):
    def test(self):
        cat = mommy.make('Recipe', title="title")

class IngredientTest(TestCase):
    def setUp(self):
        self.mL = mommy.make('Unit', name='mL', name_abbrev='mL', type=Unit.TYPE.volume, system=Unit.SYSTEM.si)
        self.l = mommy.make('Unit', name='l', name_abbrev='l', type=Unit.TYPE.volume, system=Unit.SYSTEM.si)
        self.g = mommy.make('Unit', name='gram', name_abbrev='g', type=Unit.TYPE.mass, system=Unit.SYSTEM.si)
        self.cup = mommy.make('Unit', name='cup', name_abbrev='cup', type=Unit.TYPE.volume, system=Unit.SYSTEM.imperial)

        self.egg = mommy.make('Food', name='egg', name_plural='eggs')
        self.ketchup = mommy.make('Food', name='ketchup')
        self.water = mommy.make('Food', name='water', conversion_src_unit=self.l, conversion_factor=1000)
        self.flour = mommy.make('Food', name='flour', conversion_src_unit=self.cup, conversion_factor=125)
        self.sugar = mommy.make('Food', name='sugar')

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

    def test_formatted_amount_g_to_kg_nice(self):
        ingredient = mommy.make('Ingredient', amount=3000, food=self.water, unit=self.g)
        self.assertEquals(ingredient.formatted_amount(),
                          "3 kg water")

    def test_formatted_amount_cups_tbsp_nice(self):
        ingredient = mommy.make('Ingredient', amount=1.083333333334, food=self.flour, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 cup, 1 Tbsp, 1 tsp (135 g) flour")

    def test_formatted_amount_cups_tbsp_nice(self):
        ingredient = mommy.make('Ingredient', amount=1.083333333333, food=self.flour, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 cup, 1 Tbsp, 1 tsp (135 g) flour")

    def test_formatted_amount_cups_fractions(self):
        ingredient = mommy.make('Ingredient', amount=1.5, food=self.flour, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 1/2 cup (188 g) flour")

    def test_formatted_amount_cups_fractions(self):
        ingredient = mommy.make('Ingredient', amount=1.5, food=self.flour, unit=self.cup)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 1/2 cup (188 g) flour")

    def test_formatted_amount_prep_method(self):
        sifted = mommy.make('PrepMethod', name='sifted')
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.cup, prep_method=sifted)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 cup sifted sugar")

    def test_formatted_amount_prep_method(self):
        sifted = mommy.make('PrepMethod', name='sifted')
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.cup, prep_method=sifted)
        self.assertEquals(ingredient.formatted_amount(),
                          "1 cup sifted sugar")

    def test_formatted_amount_instruction(self):
        ingredient = mommy.make('Ingredient', amount=1, food=self.sugar, unit=self.cup, instruction='fried')
        self.assertEquals(ingredient.formatted_amount(),
                          "1 cup sugar (fried)")





test_cases_nearest = {4: (
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
