from django import template

register = template.Library()


@register.filter(name='get_col')
def get_col(obj, field):
    return getattr(obj, field, '')