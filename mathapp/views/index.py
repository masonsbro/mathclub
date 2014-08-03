from django.shortcuts import render, redirect

from mathapp.models import *

# Create your views here.

def index(req):
	if 'email' in req.session:
		return render(req, "dashboard.html")
	else:
		return render(req, "landing.html")