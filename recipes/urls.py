from django.conf.urls.defaults import url, patterns
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from tagging.views import tagged_object_list
from models import Recipe

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

urlpatterns = patterns('recipes.views',
    (r'^search/$', 'search'),

    # home page
    url(r'^$', list_detail.object_list, recipe_list_info, name="recipes_home"),

    # list
    url(r'^list/$', list_detail.object_list, recipe_list_info, name="recipes_list"),

    # tag pages
    url(r'^tag/(?P<tag>[^/]+)/$',
           tagged_object_list,
           dict(queryset_or_model=Recipe, paginate_by=RECIPES_PAGINATE_BY,
               allow_empty=True, template_object_name='recipe'),
           name='recipe_list_by_tag'),

    # detail by id
    url(r'^recipes/(?P<object_id>\d+)/$', list_detail.object_detail, recipe_detail_info, name="recipe_detail_by_id"),
    # detail by slug
    url(r'^recipes/(?P<slug>[-\w]+)/$', list_detail.object_detail, recipe_detail_info, name="recipe_detail_by_slug"),

    # add
    (r'^add/$', 'recipe_add'),
    (r'^add/thanks/$', direct_to_template, {'template': 'recipes/recipe_add_thanks.html'} ),

)
