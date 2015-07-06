from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

base_urls = patterns('',
    url(r'^', include('savior.apps.savior.urls')),
)

unprefixed = url(r'', include((base_urls, '', '')))
admin_urls = url(r'^admin/', include(admin.site.urls))

urlpatterns = patterns(r'', *(unprefixed, admin_urls))
