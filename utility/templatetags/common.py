from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def getColumnSize(size):
    return {
        "sm": "col-lg-2",
        "md": "col-lg-4",
        "lg": "col-lg-8",
        "full": "col-lg-12",
    }[size]
