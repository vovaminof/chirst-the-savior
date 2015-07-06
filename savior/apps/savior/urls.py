from django.conf.urls import patterns, url

from savior.apps.savior import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='savior-index'),
)