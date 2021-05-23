import string

from django import template
from django.core import serializers
from django.db.models import QuerySet
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@stringfilter
def getColumnSize(size: string):
    return {
        "sm": "col-lg-2",
        "md": "col-lg-4",
        "lg": "col-lg-8",
        "full": "col-lg-12",
    }[size]


@register.filter(is_safe=True)
def serialize(queryset: QuerySet, id: string) -> string:

    return mark_safe(
        f"""<script type="application/json" id="{id}">{serializers.serialize('json', queryset)}</script>"""
    )
