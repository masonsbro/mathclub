from django.shortcuts import render, redirect

from mathapp.models import *

from .util import *

# Create your views here.

@check_logged_in
def login(req, context):
	return render(req, "login.html", context)

@check_logged_in
def register(req, context):
	return render(req, "register.html", context)