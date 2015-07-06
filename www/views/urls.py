from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

basepatterns = patterns('views.views',
	url(r'^$', 'index', name='index'),
)

urlpatterns = basepatterns + patterns('',

)

if getattr(settings, 'DJANGO_DEV_SERVER', False):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)