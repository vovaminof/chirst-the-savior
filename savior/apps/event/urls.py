from django.conf.urls import patterns, url

from django.conf.urls.i18n import i18n_patterns
from savior.apps.event import views

urlpatterns = patterns('',
	url(r'^$', views.get_all_events, name='event-get_all_events'),
	url(r'^(?P<event_id>[0-9]+)/(?P<occurrence_id>[0-9]+)/$', views.get_event, name='event-get_event'),
)