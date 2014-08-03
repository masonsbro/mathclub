from django.shortcuts import render, redirect
from django.core.validators import validate_email

from mathapp.models import *

from .util import *
from .const import *

# Create your views here.

@init_alerts
@check_logged_in
def login(req, context):
	if req.method == 'GET':
		return render(req, "login.html", context)
	else:
		if 'email' not in req.session:
			# Process login
			try:
				user = User.objects.get(email = req.POST['email'])
				if not user.check_password(req.POST['password']):
					raise
				req.session['email'] = req.POST['email']
				return redirect("/")
			except:
				context['danger_alerts'].append(WRONG_EMAIL_PASSWORD)
				context['email_preset'] = req.POST['email']
				return render(req, "login.html", context)
		else:
			# Already logged in
			return redirect("/")

@init_alerts
@check_logged_in
def register(req, context):
	if req.method == 'GET':
		return render(req, "register.html", context)
	else:
		if 'email' not in req.session:
			# Process registration
			try:
				validate_email(req.POST['email'])
			except:
				context['danger_alerts'].append(INVALID_EMAIL)
			if not req.POST['password']:
				context['danger_alerts'].append(INVALID_PASSWORD)
			if req.POST['password'] != req.POST['password_confirm']:
				context['danger_alerts'].append(PASSWORD_MISMATCH)
			if not context['danger_alerts']:
				try:
					user = User(email = req.POST['email'])
					user.set_password(req.POST['password'])
					user.save()
					req.session['email'] = req.POST['email']
					return redirect("/")
				except:
					context['danger_alerts'].append(EMAIL_ALREADY_EXISTS)
			context['email_preset'] = req.POST['email']
			return render(req, "register.html", context)
		else:
			# Already logged in
			return redirect("/")

@check_logged_in
def logout(req, context):
	if 'email' in req.session:
		del req.session['email']
	return redirect("/")