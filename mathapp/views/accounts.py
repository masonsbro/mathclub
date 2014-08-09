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
					user = User(email = req.POST['email'], name = req.POST['name'])
					user.set_password(req.POST['password'])
					user.save()
					# Initialize target scores
					difficulties = Difficulty.objects.all()
					for difficulty in difficulties:
						TargetScore(user = user, difficulty = difficulty).save()
					req.session['email'] = req.POST['email']
					return redirect("/")
				except:
					context['danger_alerts'].append(EMAIL_ALREADY_EXISTS)
			context['email_preset'] = req.POST['email']
			context['name_preset'] = req.POST['name']
			return render(req, "register.html", context)
		else:
			# Already logged in
			return redirect("/")

@check_logged_in
def logout(req, context):
	if 'email' in req.session:
		del req.session['email']
	return redirect("/")

@init_alerts
@check_logged_in
@only_logged_in
def account(req, context):
	if req.method == 'GET':
		return render(req, "account.html", context)
	else:
		# Process account changes
		user = context['user']
		if not user.check_password(req.POST['password_current']):
			context['danger_alerts'].append(WRONG_CURRENT_PASSWORD)
		else:
			if req.POST['email']:
				try:
					validate_email(req.POST['email'])
				except:
					context['danger_alerts'].append(INVALID_EMAIL)
				try:
					user.email = req.POST['email']
					req.session['email'] = user.email
				except:
					context['danger_alerts'].append(EMAIL_ALREADY_EXISTS)
			if req.POST['password']:
				if req.POST['password'] != req.POST['password_confirm']:
					context['danger_alerts'].append(PASSWORD_MISMATCH)
				else:
					user.set_password(req.POST['password'])
			if req.POST['name']:
				user.name = req.POST['name']
		if context['danger_alerts']:
			return render(req, "account.html", context)
		else:
			user.save()
			return redirect("/")

@init_alerts
@check_logged_in
@only_logged_in
def goals(req, context):
	if req.method == 'GET':
		return render(req, "goals.html", context)
	else:
		# Process goal changes
		user = context['user']
		# Update target scores
		difficulties = Difficulty.objects.all()
		for difficulty in difficulties:
			if req.POST['target_score_' + str(difficulty.pk)]:
				try:
					ts = TargetScore.objects.get(user = context['user'], difficulty = difficulty)
					ts.score = int(req.POST['target_score_' + str(difficulty.pk)])
					ts.save()
				except:
					context['danger_alerts'].append(INVALID_SCORE)
		if context['danger_alerts']:
			return render(req, "account.html", context)
		else:
			user.save()
			return redirect("/")
