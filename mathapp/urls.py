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
	url(r'^admind/blog/new/$', views.admin_blog_new),
	url(r'^admind/blog/edit/(?P<id>[0-9]+)/$', views.admin_blog_edit),
	url(r'^admind/blog/delete/(?P<id>[0-9]+)/$', views.admin_blog_delete),
	url(r'^admind/problems/$', views.admin_problems),
	url(r'^admind/problems/new/$', views.admin_problems_new),
	url(r'^admind/problems/edit/(?P<id>[0-9]+)/$', views.admin_problems_edit),
	url(r'^admind/problems/delete/(?P<id>[0-9]+)/$', views.admin_problems_delete),
	url(r'^admind/learn/text/$', views.admin_learn_text),
	url(r'^admind/learn/text/new/$', views.admin_learn_text_new),
	url(r'^admind/learn/text/edit/(?P<id>[0-9]+)/$', views.admin_learn_text_edit),
	url(r'^admind/learn/text/delete/(?P<id>[0-9]+)/$', views.admin_learn_text_delete),
	url(r'^admind/learn/video/$', views.admin_learn_video),
	url(r'^admind/learn/video/new/$', views.admin_learn_video_new),
	url(r'^admind/learn/video/edit/(?P<id>[0-9]+)/$', views.admin_learn_video_edit),
	url(r'^admind/learn/video/delete/(?P<id>[0-9]+)/$', views.admin_learn_video_delete),
	url(r'^blog/$', views.blog),
	url(r'^practice/$', views.practice_index),
	url(r'^practice/skill/(?P<id>[0-9]+)/$', views.practice_skill),
	url(r'^practice/difficulty/(?P<id>[0-9]+)/$', views.practice_difficulty),
	url(r'^practice/all/$', views.practice_all),
	url(r'^reset/$', views.reset),
	url(r'^learn/$', views.learn_index),
	url(r'^learn/skill/(?P<id>[0-9]+)/text/$', views.learn_skill_text),
	url(r'^learn/skill/(?P<id>[0-9]+)/video/$', views.learn_skill_video),
	url(r'^learn/difficulty/(?P<id>[0-9]+)/$', views.learn_difficulty),
	url(r'^$', views.index),
)