from django.conf.urls import patterns, url

from django.conf.urls.i18n import i18n_patterns
from savior.apps.menu import views

urlpatterns = patterns('',
	url(r'^$', views.get_index, name='menu-get_index'),
    url(r'^(about|o\-nas)/(?P<slug>[\w\-]+)/$', views.get_about, name='menu-get_about'),
    url(r'^(ministry|duszpasterstwo)/(?P<slug>[\w\-]+)/$', views.get_ministry, name='menu-get_ministry'),
    url(r'^(project|projekt)/(?P<slug>[\w\-]+)/$', views.get_project, name='menu-get_project'),
    url(r'^(course|kurs)/(?P<slug>[\w\-]+)/$', views.get_course, name='menu-get_course'),
    url(r'^contact/$', views.get_contact, name='menu-get_contact'),
)