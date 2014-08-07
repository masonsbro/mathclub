from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core import serializers
from django.http import HttpResponse

from mathapp.models import *

from .util import *
from .const import *

# Create your views here.

def learn_items_skill(req, id):
	return HttpResponse(serializers.serialize("json", LearnItem.objects.filter(skill__pk = id)))
