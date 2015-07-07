from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


admin.autodiscover()

base_urls = patterns('',
    url(r'^', include('savior.apps.savior.urls')),
)

unprefixed = url(r'', include((base_urls, '', '')))
admin_urls = url(r'^admin/', include(admin.site.urls))

urlpatterns = i18n_patterns(r'', *(unprefixed, admin_urls)) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
