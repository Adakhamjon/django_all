from django import template
register = template.Library()
@register.filter("current_path")
def current_path(request):
	path = str(request.path)
	path = path[1:-1]
	return int(path)