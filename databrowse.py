from django.contrib import databrowse
from recipes.models import *

databrowse.site.register(Recipe)
databrowse.site.register(Ingredient)
databrowse.site.register(Category)
databrowse.site.register(Source)
databrowse.site.register(FoodGroup)
databrowse.site.register(Food)
databrowse.site.register(PrepMethod)
databrowse.site.register(Photo)
databrowse.site.register(Unit)
urlpatterns += patterns('',
    (r'^databrowse/(.*)', databrowse.site.root),
    )
