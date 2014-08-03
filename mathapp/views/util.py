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