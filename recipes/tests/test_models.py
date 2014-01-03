from django.test import TestCase
from recipes.models import Recipe

from django.core.urlresolvers import reverse

from model_mommy import mommy
from mock import Mock, patch

class RecipeTest(TestCase):
    def test(self):
        cat = mommy.make('Recipe', title="title")

class IngredientTest(TestCase):
    def setUp(self):
        self.mL = mommy.make('Unit', name='mL', name_abbrev='mL')
        self.l = mommy.make('Unit', name='l', name_abbrev='l')

        self.egg = mommy.make('Food', name='egg', name_plural='eggs')
        self.ketchup = mommy.make('Food', name='ketchup')
        self.water = mommy.make('Food', name='water', conversion_src_unit=self.l, conversion_factor=1000)

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

    def test_formatted_amount_mL_range(self):
        ingredient = mommy.make('Ingredient', amount=101.0, food=self.water, unit=self.mL)
        self.assertEquals(ingredient.formatted_amount(),
                          "101 mL (101 g) water")
