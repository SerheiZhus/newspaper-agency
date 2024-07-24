from django import template
register = template.Library()


@register.filter
def newspaper_names(newspapers: list) -> str:
    return ", ".join([newspaper.title for newspaper in newspapers])
