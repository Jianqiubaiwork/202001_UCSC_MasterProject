from django import template

register = template.Library()

@register.filter
def boolean(value):
    if value == 1 or True:
        return 'Yes'
    elif value == 0 or False:
        return 'No'
    else:
        return None