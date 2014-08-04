from django.shortcuts import render, redirect
from django.core.validators import validate_email

from mathapp.models import *

from .util import *
from .const import *

# Create your views here.

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin(req, context):
	return redirect("/admind/blog/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_blog(req, context):
	context['posts'] = BlogPost.objects.order_by('-pk')
	return render(req, "admin_blog.html", context)

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_blog_new(req, context):
	if req.method == 'GET':
		return render(req, "admin_blog_new.html", context)
	else:
		# Create post
		post = BlogPost(title = req.POST['title'], body = req.POST['body'], author = context['user'])
		post.save()
		return redirect("/admind/blog/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_post
def admin_blog_edit(req, context, id):
	if req.method == 'GET':
		context['post'] = BlogPost.objects.get(pk = id)
		return render(req, "admin_blog_edit.html", context)
	else:
		# Edit post
		post = BlogPost.objects.get(pk = id)
		post.title = req.POST['title']
		post.body = req.POST['body']
		post.save()
		return redirect("/admind/blog/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_post
def admin_blog_delete(req, context, id):
	post = BlogPost.objects.get(pk = id)
	post.delete()
	return redirect("/admind/blog/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_problems(req, context):
	context['problems'] = ProblemGenerator.objects.order_by('-pk')
	return render(req, "admin_problems.html", context)

@init_alerts
@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_problems_new(req, context):
	if req.method == 'GET':
		context['difficulties'] = Difficulty.objects.order_by('pk')
		return render(req, "admin_problems_new.html", context)
	else:
		if req.POST['name']:
			name = req.POST['name']
		else:
			name = req.POST['question']
		setup = req.POST['setup'].encode('ascii', 'ignore')
		setup = setup.replace('\r\n', '\n')
		setup = setup.replace('\r', '\n')
		if not req.POST['question']:
			context['danger_alerts'].append(INVALID_QUESTION)
		if not req.POST['answer']:
			context['danger_alerts'].append(INVALID_ANSWER)
		if not req.POST['skill']:
			context['danger_alerts'].append(INVALID_SKILL)
		problem = ProblemGenerator(skill = Skill.objects.get(pk = req.POST['skill']), name = name, setup = setup,
			question = req.POST['question'], answer = req.POST['answer'], author = context['user'],
			answer_prefix = req.POST['answer_prefix'], answer_suffix = req.POST['answer_suffix'], round = 'round' in req.POST)
		try:
			problem.generate_problem()
		except:
			context['danger_alerts'].append(PROBLEM_NO_GENERATE)
		if context['danger_alerts']:
			context['skill_prefill'] = req.POST['skill']
			context['name_prefill'] = req.POST['name']
			context['setup_prefill'] = req.POST['setup']
			context['question_prefill'] = req.POST['question']
			context['answer_prefill'] = req.POST['answer']
			context['answer_prefix_prefill'] = req.POST['answer_prefix']
			context['answer_suffix_prefill'] = req.POST['answer_suffix']
			context['round_prefill'] = 'round' in req.POST
			context['difficulties'] = Difficulty.objects.order_by('pk')
			return render(req, "admin_problems_new.html", context)
		else:
			problem.save()
			return redirect("/admind/problems/")

@init_alerts
@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_problem
def admin_problems_edit(req, context, id):
	if req.method == 'GET':
		context['problem'] = ProblemGenerator.objects.get(pk = id)
		context['difficulties'] = Difficulty.objects.order_by('pk')
		return render(req, "admin_problems_edit.html", context)
	else:
		if req.POST['name']:
			name = req.POST['name']
		else:
			name = req.POST['question']
		setup = req.POST['setup'].encode('ascii', 'ignore')
		setup = setup.replace('\r\n', '\n')
		setup = setup.replace('\r', '\n')
		if not req.POST['question']:
			context['danger_alerts'].append(INVALID_QUESTION)
		if not req.POST['answer']:
			context['danger_alerts'].append(INVALID_ANSWER)
		if not req.POST['skill']:
			context['danger_alerts'].append(INVALID_SKILL)
		problem = ProblemGenerator.objects.get(pk = id)
		problem.skill = Skill.objects.get(pk = req.POST['skill'])
		problem.name = name
		problem.setup = setup
		problem.question = req.POST['question']
		problem.answer = req.POST['answer']
		problem.answer_prefix = req.POST['answer_prefix']
		problem.answer_suffix = req.POST['answer_suffix']
		problem.round = 'round' in req.POST
		try:
			problem.generate_problem()
		except:
			context['danger_alerts'].append(PROBLEM_NO_GENERATE)
		if context['danger_alerts']:
			context['difficulties'] = Difficulty.objects.order_by('pk')
			return render(req, "admin_problems_edit.html", context)
		else:
			problem.save()
			return redirect("/admind/problems/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_problem
def admin_problems_delete(req, context, id):
	problem = ProblemGenerator.objects.get(pk = id)
	problem.delete()
	return redirect("/admind/problems/")