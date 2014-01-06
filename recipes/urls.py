from django.conf.urls import url, patterns
from models import Recipe
from .views import RecipeListView, RecipeDetailView, FoodConversionListView


urlpatterns = patterns('recipes.views',
    url(r'^$', RecipeListView.as_view(), name="recipe-home"),
    url(r'^list$', RecipeListView.as_view(), name="recipe-list"),
    url(r'^food-conversion-list$', FoodConversionListView.as_view(), name="food-conversion-list"),

    # tag pages
#    url(r'^tag/(?P<tag>[^/]+)/$',
#           tagged_object_list,
#           dict(queryset_or_model=Recipe, paginate_by=RECIPES_PAGINATE_BY,
#               allow_empty=True, template_object_name='recipe'),
#           name='recipe_list_by_tag'),

    # recipe detail by id
#    url(r'^recipes/(?P<object_id>\d+)/$', list_detail.object_detail, recipe_detail_info, name="recipe_detail_by_id"),
    # recipe detail by slug
    url(r'^recipes/(?P<slug>[-\w]+)/$', RecipeDetailView.as_view(), name="recipe-detail"),

#    url(r'^categories/(?P<category_slug>[-\w]+)/$', 'recipes_in_category'),

    # add
#    url(r'^add/$', 'recipe_add', name="recipe_add"),
#    (r'^add/thanks/$', direct_to_template, {'template': 'recipes/recipe_add_thanks.html'} ),

)
