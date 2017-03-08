from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    #recipes part of the site
    url(r'', include('recipes.urls')),
    #registration module
#    url(r'^accounts/', include('registration.urls')),
    #admin site
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
]

urlpatterns += staticfiles_urlpatterns()
