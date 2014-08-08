import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

def line_has_list_item(line):
	stripped = line.lstrip()
	if stripped.startswith('* '):
		return 'ul'
	elif re.match(r'\d+\. ', stripped) is not None:
		return 'ol'
	return None

def strip_line_beginning(line):
	stripped = line.lstrip()
	if stripped.startswith('* '):
		return stripped[2:]
	elif re.match(r'\d\. ', stripped) is not None:
		return re.sub(r'^\d\. ', '', stripped)
	else:
		return line

@register.filter
@stringfilter
def listify(value):
	value = ''.join(value.split('\r'))
	lines = value.split('\n')
	value = ''
	stack = []
	cur_indent = -1
	for line in lines:
		item_type = line_has_list_item(line)
		if item_type is not None:
			# TODO
			indent = len(line) - len(line.lstrip())
			if indent > cur_indent:
				cur_indent = indent
				value += '<' + item_type + '>'
				stack.append('</' + item_type + '>')
			elif indent < cur_indent:
				cur_indent = indent
				value += stack.pop()
			value += '<li>' + strip_line_beginning(line) + '</li>'
		else:
			# Close stack and add line normally
			value += ''.join(stack[::-1])
			value += line + '\n'
			cur_indent = -1
	return mark_safe(value)
