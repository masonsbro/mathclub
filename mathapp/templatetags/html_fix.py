import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def remove_html_newlines(value):
	print value
	value = re.sub(r'>\n+<', '><', value)
	print value
	return mark_safe(value)
