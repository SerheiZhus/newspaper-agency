from django import template
register = template.Library()


@register.filter
def newspaper_names(newspapers):
    return ", ".join([newspaper.title for newspaper in newspapers])
