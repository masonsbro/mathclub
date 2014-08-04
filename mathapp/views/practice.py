from django.shortcuts import render, redirect
from django.core.validators import validate_email

from mathapp.models import *

from .util import *
from .const import *

# Create your views here.

@check_logged_in
def practice_index(req, context):
	context['difficulties'] = Difficulty.objects.order_by('pk')
	return render(req, "practice_index.html", context)

@init_alerts
@check_logged_in
@log_practice
def practice_skill(req, context, id):
	try:
		context['problem'] = random.choice(ProblemGenerator.objects.filter(skill = Skill.objects.get(pk = id)))
	except:
		context['problem'] = None
	req.session['problem'] = context['problem'].pk
	context['question'], req.session['answer'] = context['problem'].generate_problem()
	return render(req, "practice_problem.html", context)

@init_alerts
@check_logged_in
@log_practice
def practice_difficulty(req, context, id):
	try:
		context['problem'] = random.choice(ProblemGenerator.objects.filter(skill__difficulty = Difficulty.objects.get(pk = id)))
	except:
		context['problem'] = None
	req.session['problem'] = context['problem'].pk
	context['question'], req.session['answer'] = context['problem'].generate_problem()
	return render(req, "practice_problem.html", context)

@init_alerts
@check_logged_in
@log_practice
def practice_all(req, context):
	try:
		context['problem'] = random.choice(ProblemGenerator.objects.all())
	except:
		context['problem'] = None
	req.session['problem'] = context['problem'].pk
	context['question'], req.session['answer'] = context['problem'].generate_problem()
	return render(req, "practice_problem.html", context)

@check_logged_in
@only_logged_in
def reset(req, context):
	if req.method == 'POST':
		user = User.objects.get(email = req.session['email'])
		if user.check_password(req.POST['password']):
			Practice.objects.filter(user = User.objects.get(email = req.session['email'])).delete()
		else:
			return redirect("/account/")
	return redirect("/")