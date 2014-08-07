from django.shortcuts import render, redirect

from mathapp.models import *

from .util import *

# Create your views here.

@check_logged_in
def index(req, context):
	if context['user']:
		# Get unseen posts
		context['posts'] = BlogPost.objects.exclude(seen_by = context['user'])
		for post in context['posts']:
			post.seen_by.add(context['user'])
		# Get skills
		context['skills'] = Skill.objects.order_by('difficulty__pk', 'pk')
		remove_skills = []
		for skill in context['skills']:
			practices = Practice.objects.filter(user = context['user'], problem__skill = skill)[:100]
			if len(practices) == 0:
				# Don't display skills with 0 practices, but also don't modify the original list during iteration
				remove_skills.append(skill)
				continue
			skill.user_practiced = 0
			skill.total_time = 0
			skill.total_correct = 0
			for practice in practices:
				skill.user_practiced += 1
				skill.total_time += practice.time
				skill.total_correct += int(practice.correct)
			skill.user_time = skill.total_time / skill.user_practiced
			skill.user_correct = 100 * skill.total_correct / skill.user_practiced
		context['skills'] = [x for x in context['skills'] if x not in remove_skills]
		return render(req, "dashboard.html", context)
	else:
		return render(req, "landing.html", context)

@check_logged_in
@only_logged_in
def skill(req, context, id):
	context['skill'] = Skill.objects.get(pk = id)
	context['practices'] = Practice.objects.filter(user = context['user'], problem__skill = context['skill'])[:50]
	return render(req, "skill.html", context)
