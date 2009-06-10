from django.conf.urls.defaults import patterns, include
from django.views.generic.simple import direct_to_template
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    #admin site
    ('^admin/(.*)', admin.site.root),

    #contact page
    (r'^contact/$', 'recipes.views.contact' ),
    (r'^contact/thanks/$', direct_to_template, {'template': 'recipes/contactthanks.html'}),

    #recipes part of the site
    (r'^cookbook/', include('recipes.urls')),

    #redirect the root to go to the recipes site
    (r'^$', 'recipes.views.root'),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
    (r'^recipes_media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),)


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
