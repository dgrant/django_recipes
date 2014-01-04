from django.test import TestCase
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User

from model_mommy import mommy

from recipes.models import Recipe

class TestList(TestCase):

    def test_non_auth(self):
        mommy.make('Recipe')
        mommy.make('Recipe')

        url = reverse('recipe-list')
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)
        self.assertIn('object_list', resp.context)

        self.assertEquals(set([link.pk for link in resp.context['object_list']]),
                          set([1, 2]))
