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
        self.egg = mommy.make('Food', name='egg', name_plural='eggs')

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
