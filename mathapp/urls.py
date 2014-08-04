from django.conf.urls import patterns, url

from mathapp import views

urlpatterns = patterns('',
	#url(r'^(?P<course_id>[0-9]+)/$', views.courseDetails),
	url(r'^login/$', views.login),
	url(r'^register/$', views.register),
	url(r'^logout/$', views.logout),
	url(r'^account/$', views.account),
	url(r'^admind/$', views.admin),
	url(r'^admind/blog/$', views.admin_blog),
	url(r'^admind/problems/$', views.admin_problems),
	url(r'^$', views.index),
)