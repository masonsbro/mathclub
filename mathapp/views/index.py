from django.shortcuts import render, redirect

from mathapp.models import *

from .util import *

# Create your views here.

@check_logged_in
def index(req, context):
	if 'email' in req.session:
		context['posts'] = BlogPost.objects.exclude(seen_by = context['user'])
		for post in context['posts']:
			post.seen_by.add(context['user'])
		return render(req, "dashboard.html", context)
	else:
		return render(req, "landing.html", context)