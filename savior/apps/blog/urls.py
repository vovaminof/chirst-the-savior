from django.conf.urls import patterns, url

from savior.apps.blog import views

urlpatterns = patterns('',
	url(r'^$', views.get_all_posts, name='blog-get_all_posts'),
	url(r'^(?P<post_id>[0-9]+)/$', views.get_post, name='blog-get_post'),
)