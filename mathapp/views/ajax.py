import datetime
import json

from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Avg
from django.utils import timezone

from mathapp.models import *

from .util import *
from .const import *

# Create your views here.

def learn_items_skill(req, id):
	return HttpResponse(serializers.serialize("json", LearnItem.objects.filter(skill__pk = id)))

@check_logged_in
@only_logged_in
def dashboard_chart(req, context):
	try:
		cur_day = Practice.objects.filter(user = context['user']).order_by('date')[0].date.date()
	except:
		# No practices yet
		return HttpResponse('[]')
	now = timezone.now().date()
	days = [['Date', '% Correct', 'Time']]
	while cur_day <= now:
		practices = Practice.objects.filter(date__lte = cur_day)[0:500]
		correct = 0
		for practice in practices:
			if practice.correct: correct += 1
		days.append((cur_day.strftime('%B %d').replace(' 0', ' '),
			correct * 100 / practices.count(),
			int(practices.aggregate(Avg('time'))['time__avg'] * 10) / 10.0))
		cur_day += datetime.timedelta(1)
	return HttpResponse(json.dumps(days))

@check_logged_in
@only_logged_in
def skill_chart(req, context, id):
	try:
		cur_day = Practice.objects.filter(user = context['user']).order_by('date')[0].date.date()
	except:
		# No practices yet
		return HttpResponse('[]')
	now = timezone.now().date()
	days = [['Date', '% Correct', 'Time']]
	while cur_day <= now:
		practices = Practice.objects.filter(date__lte = cur_day)[0:50]
		correct = 0
		for practice in practices:
			if practice.correct: correct += 1
		days.append((cur_day.strftime('%B %d').replace(' 0', ' '),
			correct * 100 / practices.count(),
			int(practices.aggregate(Avg('time'))['time__avg'] * 10) / 10.0))
		cur_day += datetime.timedelta(1)
	return HttpResponse(json.dumps(days))

@check_logged_in
@only_logged_in
def problem_chart(req, context, id):
	try:
		cur_day = Practice.objects.filter(user = context['user']).order_by('date')[0].date.date()
	except:
		# No practices yet
		return HttpResponse('[]')
	now = timezone.now().date()
	days = [['Date', '% Correct', 'Time']]
	while cur_day <= now:
		practices = Practice.objects.filter(date__lte = cur_day)[0:10]
		correct = 0
		for practice in practices:
			if practice.correct: correct += 1
		days.append((cur_day.strftime('%B %d').replace(' 0', ' '),
			correct * 100 / practices.count(),
			int(practices.aggregate(Avg('time'))['time__avg'] * 10) / 10.0))
		cur_day += datetime.timedelta(1)
	return HttpResponse(json.dumps(days))
