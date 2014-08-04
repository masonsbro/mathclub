from django.shortcuts import render, redirect
from django.core.validators import validate_email

from mathapp.models import *

from .util import *
from .const import *

# Create your views here.

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin(req, context):
	return render(req, "admin.html", context)