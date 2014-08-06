import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def add_video_containers(value):
	value = re.sub(r'(<iframe .+></iframe>)', r'<div class="video-container">\1</div>', value)
	return mark_safe(value)
