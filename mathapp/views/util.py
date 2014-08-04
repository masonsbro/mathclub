from django.shortcuts import render, redirect

from mathapp.models import *

from .const import *

def check_logged_in(func):
	def wrapper(req, context = None, *args, **kwargs):
		if context is None:
			context = {}
		if 'email' in req.session:
			context['user'] = User.objects.get(email = req.session['email'])
		else:
			context['user'] = None
		return func(req, context, *args, **kwargs)
	return wrapper

def only_logged_in(func):
	def wrapper(req, context = None, *args, **kwargs):
		if context is None:
			context = {}
		if 'user' in context or 'email' in req.session:
			return func(req, context, *args, **kwargs)
		else:
			return redirect("/")
	return wrapper

def only_admin_or_contrib(func):
	def wrapper(req, context, *args, **kwargs):
		if context['user'].admin or context['user'].contributor:
			return func(req, context, *args, **kwargs)
		else:
			return redirect("/")
	return wrapper

def must_own_post(func):
	def wrapper(req, context, id, *args, **kwargs):
		if context['user'].admin or BlogPost.objects.get(pk = id).author == context['user']:
			return func(req, context, id, *args, **kwargs)
		else:
			return redirect("/")
	return wrapper

def must_own_problem(func):
	def wrapper(req, context, id, *args, **kwargs):
		if context['user'].admin or ProblemGenerator.objects.get(pk = id).author == context['user']:
			return func(req, context, id, *args, **kwargs)
		else:
			return redirect("/")
	return wrapper

def init_alerts(func):
	def wrapper(req, context = None, *args, **kwargs):
		if context is None:
			context = {}
		context['success_alerts'] = []
		context['info_alerts'] = []
		context['warning_alerts'] = []
		context['danger_alerts'] = []
		return func(req, context, *args, **kwargs)
	return wrapper

def check_answer(correct, check, round):
	try:
		if round:
			return abs(int(check) - float(correct)) < float(correct) / 20
		try:
			return float(correct) == float(check)
		except:
			pass
		parts = check.split(' ')
		if len(parts) == 1:
			part = parts[0]
			parts = part.split('/')
			return float(correct) == float(parts[0]) / float(parts[1])
		elif len(parts) == 2:
			intPart = parts[0]
			fracPart = parts[1]
			fracs = fracPart.split('/')
			return float(correct) == (float(intPart) + float(fracs[0]) / float(fracs[1]))
		return False
	except:
		return False

def log_practice(func):
	def wrapper(req, context, *args, **kwargs):
		if req.method == 'POST':
			# Log answer and add alert
			problem = ProblemGenerator.objects.get(pk = req.session['problem'])
			correct = check_answer(req.session['answer'], req.POST['answer'], problem.round)
			if 'email' in req.session:
				practice = Practice(user = context['user'], problem = problem,
					correct = correct, time = req.POST['time'])
				practice.save()
			else:
				context['warning_alerts'].append(NO_PROGRESS)
			if correct:
				context['success_alerts'].append(CORRECT_ANSWER)
			else:
				context['danger_alerts'].append(INCORRECT_ANSWER % req.session['answer'])
		return func(req, context, *args, **kwargs)
	return wrapper