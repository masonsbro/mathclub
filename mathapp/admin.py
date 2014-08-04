from django.contrib import admin

from mathapp.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(BlogPost)
admin.site.register(Difficulty)
admin.site.register(Skill)
admin.site.register(ProblemGenerator)
admin.site.register(Practice)