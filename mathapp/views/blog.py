from django.shortcuts import render, redirect
from django.core.validators import validate_email

from mathapp.models import *

from .util import *
from .const import *

# Create your views here.

@check_logged_in
def blog(req, context):
	context['posts'] = BlogPost.objects.order_by('-pk')
	return render(req, "blog.html", context)