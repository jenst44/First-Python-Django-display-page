from django.conf.urls import patterns, url
from apps.interests import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<user_id>\d+)/$', views.show, name='show'),
)