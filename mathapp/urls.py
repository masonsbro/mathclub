from django.conf.urls import patterns, url

from mathapp import views

urlpatterns = patterns('',
	#url(r'^(?P<course_id>[0-9]+)/$', views.courseDetails),
	url(r'^login/$', views.login),
	url(r'^register/$', views.register),
	url(r'^logout/$', views.logout),
	url(r'^account/$', views.account),
	url(r'^goals/$', views.goals),
	url(r'^admind/$', views.admin),
	url(r'^admind/blog/$', views.admin_blog),
	url(r'^admind/blog/new/$', views.admin_blog_new),
	url(r'^admind/blog/edit/(?P<id>[0-9]+)/$', views.admin_blog_edit),
	url(r'^admind/blog/delete/(?P<id>[0-9]+)/$', views.admin_blog_delete),
	url(r'^admind/problems/$', views.admin_problems),
	url(r'^admind/problems/new/$', views.admin_problems_new),
	url(r'^admind/problems/edit/(?P<id>[0-9]+)/$', views.admin_problems_edit),
	url(r'^admind/problems/delete/(?P<id>[0-9]+)/$', views.admin_problems_delete),
	url(r'^admind/learn/$', views.admin_learn),
	url(r'^admind/learn/new/$', views.admin_learn_new),
	url(r'^admind/learn/edit/(?P<id>[0-9]+)/$', views.admin_learn_edit),
	url(r'^admind/learn/delete/(?P<id>[0-9]+)/$', views.admin_learn_delete),
	url(r'^admind/update/$', views.update_target_scores),
	url(r'^blog/$', views.blog),
	url(r'^practice/$', views.practice_index),
	url(r'^practice/skill/(?P<id>[0-9]+)/$', views.practice_skill),
	url(r'^practice/difficulty/(?P<id>[0-9]+)/$', views.practice_difficulty),
	url(r'^practice/all/$', views.practice_all),
	url(r'^reset/$', views.reset),
	url(r'^learn/$', views.learn_index),
	url(r'^learn/item/(?P<id>[0-9]+)/$', views.learn_item),
	url(r'^learn/skill/(?P<id>[0-9]+)/$', views.learn_skill),
	url(r'^learn/difficulty/(?P<id>[0-9]+)/$', views.learn_difficulty),
	url(r'^skill/(?P<id>[0-9]+)/$', views.skill),
	url(r'^problem/(?P<id>[0-9]+)/$', views.problem),
	url(r'^ajax/learn_items/skill/(?P<id>[0-9]+)/$', views.learn_items_skill),
	url(r'^ajax/dashboard_chart/$', views.dashboard_chart),
	url(r'^ajax/problem_chart/(?P<id>[0-9]+)/$', views.problem_chart),
	url(r'^ajax/skill_chart/(?P<id>[0-9]+)/$', views.skill_chart),
	url(r'^$', views.index),
)
