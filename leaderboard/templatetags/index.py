from django import template
register = template.Library()

@register.filter
def getRank(indexable, value):
    return indexable.index(value) + 1