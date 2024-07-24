from django import template
register = template.Library()


@register.filter
def unique_redactor(topic) -> set:
    redactors = set()
    for redactor in topic.newspapers.all():
        redactors.update(redactor.publishers.all())
    return redactors
