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
		print req.POST
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
		if int(req.POST['skill']) == -1:
			context['danger_alerts'].append(INVALID_SKILL)
		try:
			problem = ProblemGenerator(skill = Skill.objects.get(pk = req.POST['skill']), name = name, setup = setup,
				question = req.POST['question'], answer = req.POST['answer'], author = context['user'],
				answer_prefix = req.POST['answer_prefix'], answer_suffix = req.POST['answer_suffix'], round = 'round' in req.POST)
			try:
				problem.generate_problem()
				problem.save()
				for item in req.POST['learn_item']:
					problem.learn_item.add(LearnItem.objects.get(pk = item))
			except:
				context['danger_alerts'].append(PROBLEM_NO_GENERATE)
		except:
			context['danger_alerts'].append(GENERIC_ERROR)
		if context['danger_alerts']:
			context['skill_prefill'] = int(req.POST['skill'])
			context['learn_item_prefill'] = map(int, req.POST['learn_item'])
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
		problem.learn_item.empty()
		for item in req.POST['learn_item']:
			problem.learn_item.add(LearnItem.objects.get(pk = item))
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
			context['problem'] = problem
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

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_learn(req, context):
	context['items'] = LearnItem.objects.order_by('-pk')
	return render(req, "admin_learn.html", context)

@init_alerts
@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_learn_new(req, context):
	if req.method == 'GET':
		context['difficulties'] = Difficulty.objects.order_by('pk')
		return render(req, "admin_learn_new.html", context)
	else:
		# Create learn item
		if int(req.POST['skill']) == -1:
			context['danger_alerts'].append(INVALID_SKILL)
		if not req.POST['title']:
			context['danger_alerts'].append(INVALID_TITLE)
		if not req.POST['body']:
			context['danger_alerts'].append(INVALID_BODY)
		try:
			item = LearnItem(title = req.POST['title'], author = context['user'], skill = Skill.objects.get(pk = req.POST['skill']), body = req.POST['body'])
		except:
			pass
		if context['danger_alerts']:
			context['skill_prefill'] = int(req.POST['skill'])
			context['title_prefill'] = req.POST['title']
			context['body_prefill'] = req.POST['body']
			context['difficulties'] = Difficulty.objects.order_by('pk')
			return render(req, "admin_learn_new.html", context)
		else:
			item.save()
			return redirect("/admind/learn/")

@init_alerts
@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_learn_item
def admin_learn_edit(req, context, id):
	if req.method == 'GET':
		context['item'] = LearnItem.objects.get(pk = id)
		context['difficulties'] = Difficulty.objects.order_by('pk')
		return render(req, "admin_learn_edit.html", context)
	else:
		# Save edits
		item = LearnItem.objects.get(pk = id)
		try:
			item.skill = Skill.objects.get(pk = req.POST['skill'])
		except:
			context['danger_alerts'].append(INVALID_SKILL)
		item.title = req.POST['title']
		item.body = req.POST['body']
		if not req.POST['title']:
			context['danger_alerts'].append(INVALID_TITLE)
		if not req.POST['body']:
			context['danger_alerts'].append(INVALID_BODY)
		if context['danger_alerts']:
			context['difficulties'] = Difficulty.objects.order_by('pk')
			context['item'] = item
			return render(req, "admin_learn_edit.html", context)
		else:
			item.save()
			return redirect("/admind/learn/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_learn_item
def admin_learn_delete(req, context, id):
	item = LearnItem.objects.get(pk = id)
	item.delete()
	return redirect("/admind/learn/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def update_target_scores(req, context):
	users = User.objects.all()
	difficulties = Difficulty.objects.all()
	for user in users:
		for difficulty in difficulties:
			TargetScore.objects.get_or_create(user = user, difficulty = difficulty)
	return redirect("/admind/blog/")
