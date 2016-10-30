from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


admin.autodiscover()

base_urls = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^service/', include('savior.apps.service.urls')),
    url(r'^savior/', include('savior.apps.savior.urls')),
    url(r'^events/', include('savior.apps.event.urls')),
    url(r'^blog/', include('savior.apps.blog.urls')),
    url(r'^resources/', include('savior.apps.resource.urls')),
    url(r'^', include('savior.apps.menu.urls')),
)

unprefixed = url(r'', include((base_urls, '', '')))
admin_urls = url(r'^admin/', include(admin.site.urls))

urlpatterns = i18n_patterns(r'', *(unprefixed, admin_urls)) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
