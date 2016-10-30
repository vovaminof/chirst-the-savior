from django.conf.urls import patterns, url

from savior.apps.resource import views

urlpatterns = patterns('',
	url(r'^$', views.get_all_resources, name='resource-get_all_resources')
)