from django import template
register = template.Library()


@register.filter
def unique_topics(redactor):
    topics = set()
    for newspaper in redactor.newspapers.all():
        topics.update(newspaper.topic.all())
    return topics
