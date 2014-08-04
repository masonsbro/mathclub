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
	return redirect("/admind/blog/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_blog(req, context):
	context['posts'] = BlogPost.objects.order_by('-pk')
	return render(req, "admin_blog.html", context)

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_blog_new(req, context):
	if req.method == 'GET':
		return render(req, "admin_blog_new.html", context)
	else:
		# Create post
		post = BlogPost(title = req.POST['title'], body = req.POST['body'], author = context['user'])
		post.save()
		return redirect("/admind/blog/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_post
def admin_blog_edit(req, context, id):
	if req.method == 'GET':
		context['post'] = BlogPost.objects.get(pk = id)
		return render(req, "admin_blog_edit.html", context)
	else:
		# Edit post
		post = BlogPost.objects.get(pk = id)
		post.title = req.POST['title']
		post.body = req.POST['body']
		post.save()
		return redirect("/admind/blog/")

@check_logged_in
@only_logged_in
@only_admin_or_contrib
@must_own_post
def admin_blog_delete(req, context, id):
	pass

@check_logged_in
@only_logged_in
@only_admin_or_contrib
def admin_problems(req, context):
	return render(req, "admin_problems.html", context)