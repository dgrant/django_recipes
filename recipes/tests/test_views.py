from django.test import TestCase
from django.urls import reverse

from model_mommy import mommy


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
