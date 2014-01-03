from django.test import TestCase
from recipes.models import Unit

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

