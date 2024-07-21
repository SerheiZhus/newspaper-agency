from django import template
register = template.Library()


@register.filter
def unique_publisher(newspaper):
    return ", ".join([publisher.first_name + ' ' + publisher.last_name for publisher in newspaper.publishers.all()])
