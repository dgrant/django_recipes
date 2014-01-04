from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #recipes part of the site
    url(r'^cookbook/', include('recipes.urls')),
    #redirect the root to go to the recipes site
    url(r'^$', 'recipes.views.root'),
    #registration module
#    url(r'^accounts/', include('registration.urls')),
    #admin site
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

urlpatterns += staticfiles_urlpatterns()
