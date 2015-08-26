from django.conf.urls import patterns, url

from django.conf.urls.i18n import i18n_patterns
from savior.apps.savior import views

urlpatterns = patterns('',
    url(r'^send-request/$', views.send_request, name='savior-send-request'),
)