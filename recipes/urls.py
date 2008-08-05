from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from cookbook.recipes.models import Recipe

# Need this function so that len(Recipes.objects.all()) can get re-evaluated repeatedly
def getNumRecipes():
    return len(Recipe.objects.all())

RECIPES_PAGINATE_BY = 10

recipe_list_info = {
    "queryset": Recipe.objects.all(),
    "template_object_name" : "recipe",
    "paginate_by": RECIPES_PAGINATE_BY,
}

recipe_detail_info = {
    "queryset": Recipe.objects.all(),
    "template_object_name" : "recipe",
}

urlpatterns = patterns('cookbook.recipes.views',
    (r'^search/$', 'search'),

    # list
    (r'^recipes/$', list_detail.object_list, recipe_list_info),

    # detail
    (r'^recipe/(?P<object_id>\d+)/$', list_detail.object_detail, recipe_detail_info),

    # add
    (r'^recipe/add/$', 'recipe_add'),
    (r'^recipe/add/thanks/$', direct_to_template, {'template': 'recipes/recipe_add_thanks.html'} ),

)
