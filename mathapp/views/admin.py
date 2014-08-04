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
		if int(req.POST['skill']) == -1:
			context['danger_alerts'].append(INVALID_SKILL)
		try:
			problem = ProblemGenerator(skill = Skill.objects.get(pk = req.POST['skill']), name = name, setup = setup,
				question = req.POST['question'], answer = req.POST['answer'], author = context['user'],
				answer_prefix = req.POST['answer_prefix'], answer_suffix = req.POST['answer_suffix'], round = 'round' in req.POST)
			try:
				problem.generate_problem()
			except:
				context['danger_alerts'].append(PROBLEM_NO_GENERATE)
		except:
			pass
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
def admin_learn_text(req, context):
	context['items'] = LearnText.objects.order_by('-pk')
	return render(req, "admin_learn_text.html", context)

@init_alerts
@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_learn_text_new(req, context):
	if req.method == 'GET':
		context['difficulties'] = Difficulty.objects.order_by('pk')
		return render(req, "admin_learn_text_new.html", context)
	else:
		# Create learn text
		if int(req.POST['skill']) == -1:
			context['danger_alerts'].append(INVALID_SKILL)
		if not req.POST['title']:
			context['danger_alerts'].append(INVALID_TITLE)
		if not req.POST['body']:
			context['danger_alerts'].append(INVALID_BODY)
		try:
			text = LearnText(title = req.POST['title'], author = context['user'], skill = Skill.objects.get(pk = req.POST['skill']), body = req.POST['body'])
		except:
			pass
		if context['danger_alerts']:
			context['skill_prefill'] = req.POST['skill']
			context['title_prefill'] = req.POST['title']
			context['body_prefill'] = req.POST['body']
			context['difficulties'] = Difficulty.objects.order_by('pk')
			return render(req, "admin_learn_text_new.html", context)
		else:
			text.save()
			return redirect("/admind/learn/text/")

@init_alerts
@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_text
def admin_learn_text_edit(req, context, id):
	if req.method == 'GET':
		context['text'] = LearnText.objects.get(pk = id)
		context['difficulties'] = Difficulty.objects.order_by('pk')
		return render(req, "admin_learn_text_edit.html", context)
	else:
		# Save edits
		text = LearnText.objects.get(pk = id)
		try:
			text.skill = Skill.objects.get(pk = req.POST['skill'])
		except:
			context['danger_alerts'].append(INVALID_SKILL)
		text.title = req.POST['title']
		text.body = req.POST['body']
		if not req.POST['title']:
			context['danger_alerts'].append(INVALID_TITLE)
		if not req.POST['body']:
			context['danger_alerts'].append(INVALID_BODY)
		if context['danger_alerts']:
			context['difficulties'] = Difficulty.objects.order_by('pk')
			context['text'] = text
			return render(req, "admin_learn_text_edit.html", context)
		else:
			text.save()
			return redirect("/admind/learn/text/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_text
def admin_learn_text_delete(req, context, id):
	text = LearnText.objects.get(pk = id)
	text.delete()
	return redirect("/admind/learn/text/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_learn_video(req, context):
	context['items'] = LearnVideo.objects.order_by('-pk')
	return render(req, "admin_learn_video.html", context)

@init_alerts
@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_learn_video_new(req, context):
	if req.method == 'GET':
		context['difficulties'] = Difficulty.objects.order_by('pk')
		return render(req, "admin_learn_video_new.html", context)
	else:
		# Create learn text
		if int(req.POST['skill']) == -1:
			context['danger_alerts'].append(INVALID_SKILL)
		if not req.POST['title']:
			context['danger_alerts'].append(INVALID_TITLE)
		if not req.POST['code']:
			context['danger_alerts'].append(INVALID_CODE)
		try:
			video = LearnVideo(title = req.POST['title'], author = context['user'],
				skill = Skill.objects.get(pk = req.POST['skill']), code = req.POST['code'])
		except:
			pass
		if context['danger_alerts']:
			context['skill_prefill'] = req.POST['skill']
			context['title_prefill'] = req.POST['title']
			context['code_prefill'] = req.POST['code']
			context['difficulties'] = Difficulty.objects.order_by('pk')
			return render(req, "admin_learn_video_new.html", context)
		else:
			video.save()
			return redirect("/admind/learn/video/")

@init_alerts
@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_video
def admin_learn_video_edit(req, context, id):
	if req.method == 'GET':
		context['video'] = LearnVideo.objects.get(pk = id)
		context['difficulties'] = Difficulty.objects.order_by('pk')
		return render(req, "admin_learn_video_edit.html", context)
	else:
		# Save edits
		video = LearnVideo.objects.get(pk = id)
		try:
			video.skill = Skill.objects.get(pk = req.POST['skill'])
		except:
			context['danger_alerts'].append(INVALID_SKILL)
		video.title = req.POST['title']
		video.code = req.POST['code']
		if not req.POST['title']:
			context['danger_alerts'].append(INVALID_TITLE)
		if not req.POST['code']:
			context['danger_alerts'].append(INVALID_CODE)
		if context['danger_alerts']:
			context['difficulties'] = Difficulty.objects.order_by('pk')
			context['video'] = video
			return render(req, "admin_learn_video_edit.html", context)
		else:
			video.save()
			return redirect("/admind/learn/video/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_video
def admin_learn_video_delete(req, context, id):
	video = LearnVideo.objects.get(pk = id)
	video.delete()
	return redirect("/admind/learn/video/")