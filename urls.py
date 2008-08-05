from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    ('^admin/(.*)', admin.site.root),

    (r'^contact/$', 'contact' ),
    (r'^contact/thanks/$', direct_to_template, {'template': 'contact_thanks.html'}),

    (r'^recipes/', include('recipes.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),)
