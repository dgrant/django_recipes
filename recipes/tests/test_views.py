from django.test import TestCase
from django.urls import reverse

from model_mommy import mommy

from recipes.models import Unit


class TestRecipeList(TestCase):

    def test_list(self):
        mommy.make('Recipe')
        mommy.make('Recipe')

        url = reverse('recipe-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('object_list', resp.context)

        self.assertEqual(set([link.pk for link in resp.context['object_list']]),
                         set([1, 2]))


class TestRecipeDetail(TestCase):

    def setUp(self):
        # Create units for testing
        self.cup = mommy.make('Unit', name='cup', type=Unit.TYPE.volume, system=Unit.SYSTEM.imperial)
        self.gram = mommy.make('Unit', name='gram', type=Unit.TYPE.mass, system=Unit.SYSTEM.si)

        # Create a category (required for Recipe)
        self.category = mommy.make('Category', name='Desserts')

        # Create foods
        self.flour = mommy.make('Food', name='flour', name_sorted='flour',
                                conversion_src_unit=self.cup, conversion_factor=120.0)
        self.sugar = mommy.make('Food', name='sugar', name_sorted='sugar',
                                conversion_src_unit=self.cup, conversion_factor=200.0)

        # Create a recipe
        self.recipe = mommy.make('Recipe', title='Test Cake', slug='test-cake', category=self.category)

        # Create a direction
        self.direction = mommy.make('Direction', recipe=self.recipe, text='Mix ingredients')

        # Create ingredients
        self.ingredient1 = mommy.make('Ingredient', recipe=self.recipe, direction=self.direction,
                                      food=self.flour, amount=2.0, unit=self.cup)
        self.ingredient2 = mommy.make('Ingredient', recipe=self.recipe, direction=self.direction,
                                      food=self.sugar, amount=1.0, unit=self.cup)

    def test_detail_view_returns_200(self):
        """Test that recipe detail view returns 200 status code"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_detail_view_has_recipe_in_context(self):
        """Test that recipe object is available in context"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        resp = self.client.get(url)
        self.assertIn('recipe', resp.context)
        self.assertEqual(resp.context['recipe'].title, 'Test Cake')

    def test_detail_view_default_scale_is_one(self):
        """Test that recipe has scale of 1.0 when no scale parameter provided"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        resp = self.client.get(url)
        recipe = resp.context['recipe']
        self.assertEqual(recipe.scale, 1.0)

    def test_detail_view_with_scale_parameter(self):
        """Test that scale parameter correctly sets recipe.scale"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        resp = self.client.get(url, {'scale': '2.0'})
        recipe = resp.context['recipe']
        self.assertEqual(recipe.scale, 2.0)

    def test_detail_view_with_half_scale(self):
        """Test that scale parameter works with fractional values"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        resp = self.client.get(url, {'scale': '0.5'})
        recipe = resp.context['recipe']
        self.assertEqual(recipe.scale, 0.5)

    def test_detail_view_with_triple_scale(self):
        """Test that scale parameter works with larger values"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        resp = self.client.get(url, {'scale': '3.0'})
        recipe = resp.context['recipe']
        self.assertEqual(recipe.scale, 3.0)

    def test_detail_view_with_invalid_scale_raises_error(self):
        """Test that invalid scale parameter raises ValueError"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        with self.assertRaises(ValueError):
            self.client.get(url, {'scale': 'invalid'})

    def test_detail_view_nonexistent_recipe_returns_404(self):
        """Test that requesting a non-existent recipe returns 404"""
        url = reverse('recipe-detail', kwargs={'slug': 'nonexistent-recipe'})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_scaling_affects_ingredient_amounts(self):
        """Test that scaling parameter affects ingredient amounts in get_text()"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})

        # Get recipe with default scale (1.0)
        resp = self.client.get(url)
        recipe = resp.context['recipe']
        text_data = recipe.get_text()

        # Get recipe with scale 2.0
        resp_scaled = self.client.get(url, {'scale': '2.0'})
        recipe_scaled = resp_scaled.context['recipe']
        text_data_scaled = recipe_scaled.get_text()

        # Both should have the same structure, but different amounts
        self.assertEqual(len(text_data), len(text_data_scaled))
        # The formatted amounts should be different (due to scaling)
        self.assertNotEqual(text_data[0][1][0][0], text_data_scaled[0][1][0][0])

    def test_scaling_with_serving_string(self):
        """Test that scaling affects serving values"""
        # Create a serving string with placeholder
        serving_string = mommy.make('ServingString', text='Makes %s servings')
        recipe = mommy.make('Recipe', title='Cookies', slug='cookies', category=self.category,
                           serving_string=serving_string, serving_value=12)

        # Test with default scale
        url = reverse('recipe-detail', kwargs={'slug': 'cookies'})
        resp = self.client.get(url)
        recipe_obj = resp.context['recipe']
        serving = recipe_obj.get_serving()
        self.assertEqual(serving, 'Makes 12 servings')

        # Test with double scale
        resp_scaled = self.client.get(url, {'scale': '2.0'})
        recipe_scaled = resp_scaled.context['recipe']
        serving_scaled = recipe_scaled.get_serving()
        self.assertEqual(serving_scaled, 'Makes 24 servings')

    def test_scale_parameter_zero(self):
        """Test that scale=0 works (edge case)"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        resp = self.client.get(url, {'scale': '0'})
        recipe = resp.context['recipe']
        self.assertEqual(recipe.scale, 0.0)

    def test_scale_parameter_very_small(self):
        """Test that very small scale values work"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        resp = self.client.get(url, {'scale': '0.25'})
        recipe = resp.context['recipe']
        self.assertEqual(recipe.scale, 0.25)

    def test_scale_parameter_very_large(self):
        """Test that very large scale values work"""
        url = reverse('recipe-detail', kwargs={'slug': 'test-cake'})
        resp = self.client.get(url, {'scale': '100'})
        recipe = resp.context['recipe']
        self.assertEqual(recipe.scale, 100.0)


class TestFoodConversionList(TestCase):
    def setUp(self):
        self.cups = mommy.make('Unit', name='cups')

    def test_list(self):
        mommy.make('Food')  # 1
        mommy.make('Food', name_sorted='zoodles', conversion_src_unit=self.cups, conversion_factor=125.)  # 2
        mommy.make('Food', name_sorted='apples', conversion_src_unit=self.cups, conversion_factor=60.)  # 3

        url = reverse('food-conversion-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('object_list', resp.context)

        self.assertEqual([link.pk for link in resp.context['object_list']],
                         [3, 2])
