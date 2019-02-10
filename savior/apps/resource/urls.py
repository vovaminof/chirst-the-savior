from django.conf.urls import patterns, url

from savior.apps.resource import views

urlpatterns = patterns('',
	url(r'^$', views.get_all_resources, name='resource-get_all_resources'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.get_book, name='resource-get_book'),
)
