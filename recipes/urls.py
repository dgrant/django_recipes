from django.conf.urls import url

from .views import RecipeListView, RecipeDetailView, FoodConversionListView

urlpatterns = [
    url(r'^$', RecipeListView.as_view(), name="recipe-home"),
    url(r'^list$', RecipeListView.as_view(), name="recipe-list"),
    url(r'^food-conversion-list$', FoodConversionListView.as_view(), name="food-conversion-list"),

    # recipe detail by slug
    url(r'^recipes/(?P<slug>[-\w]+)/$', RecipeDetailView.as_view(), name="recipe-detail"),
]
