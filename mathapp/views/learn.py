from django.shortcuts import render, redirect
from django.core.validators import validate_email

from mathapp.models import *

from .util import *
from .const import *

# Create your views here.

@check_logged_in
def learn_index(req, context):
	context['difficulties'] = Difficulty.objects.order_by('pk')
	return render(req, "learn_index.html", context)

@check_logged_in
def learn_skill_text(req, context, id):
	context['skill'] = Skill.objects.get(pk = id)
	context['text'] = True
	context['items'] = LearnText.objects.filter(skill = context['skill'])
	return render(req, "learn_skill.html", context)

@check_logged_in
def learn_skill_video(req, context, id):
	context['skill'] = Skill.objects.get(pk = id)
	context['video'] = True
	context['items'] = LearnVideo.objects.filter(skill = context['skill'])
	return render(req, "learn_skill.html", context)

@check_logged_in
def learn_difficulty(req, context, id):
	context['difficulty'] = Difficulty.objects.get(pk = id)
	return render(req, "learn_difficulty.html", context)