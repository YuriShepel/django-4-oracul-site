from django import template

from ..models import TarotSuits

register = template.Library()


@register.simple_tag()
def get_suits():
    return TarotSuits.objects.all().order_by('id')
