from django.shortcuts import render, redirect
from django.core.validators import validate_email

from mathapp.models import *

from .util import *
from .const import *

# Create your views here.

@check_logged_in
def blog(req, context):
	context['posts'] = BlogPost.objects.order_by('-pk')
	for post in context['posts']:
		if context['user']:
			post.seen_by.add(context['user'])
	return render(req, "blog.html", context)
