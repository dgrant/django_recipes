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
    #(r'^$', include('recipes.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
    (r'^recipes_media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),)
