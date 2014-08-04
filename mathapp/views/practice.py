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
	context['problem'] = random.choice(ProblemGenerator.objects.filter(skill = Skill.objects.get(pk = id)))
	req.session['problem'] = context['problem'].pk
	context['question'], req.session['answer'] = context['problem'].generate_problem()
	return render(req, "practice_problem.html", context)

@init_alerts
@check_logged_in
@log_practice
def practice_difficulty(req, context, id):
	context['problem'] = random.choice(ProblemGenerator.objects.filter(skill__difficulty = Difficulty.objects.get(pk = id)))
	req.session['problem'] = context['problem'].pk
	context['question'], req.session['answer'] = context['problem'].generate_problem()
	return render(req, "practice_problem.html", context)

@init_alerts
@check_logged_in
@log_practice
def practice_all(req, context):
	context['problem'] = random.choice(ProblemGenerator.objects.all())
	req.session['problem'] = context['problem'].pk
	context['question'], req.session['answer'] = context['problem'].generate_problem()
	return render(req, "practice_problem.html", context)

@check_logged_in
@only_logged_in
def reset(req, context):
	Practice(user = User.get(email = req.session['email'])).delete()
	return redirect("/")