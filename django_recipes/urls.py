from django.urls import include, path
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    #recipes part of the site
    path(r'', include('recipes.urls')),
    #registration module
#    url(r'accounts/', include('registration.urls')),
    #admin site
    path(r'admin/', admin.site.urls),
    path(r'admin/doc/', include('django.contrib.admindocs.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += staticfiles_urlpatterns()
