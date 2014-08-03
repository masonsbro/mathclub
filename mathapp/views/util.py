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