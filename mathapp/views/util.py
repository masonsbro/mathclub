from django.shortcuts import render, redirect

from mathapp.models import *

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

def log_practice(func):
	def wrapper(req, context, *args, **kwargs):
		if req.method == 'POST':
			# Log answer and add alert
			pass
		return func(req, context, *args, **kwargs)
	return wrapper