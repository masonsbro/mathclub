from django.shortcuts import render, redirect

from mathapp.models import *

from .util import *

# Create your views here.

@check_logged_in
def index(req, context):
	if 'email' in req.session:
		return render(req, "dashboard.html", context)
	else:
		return render(req, "landing.html", context)