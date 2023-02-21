from django import template

from tarot_cards.models import TarotSuits

register = template.Library()


@register.simple_tag()
def get_suits():
    return TarotSuits.objects.all().order_by('id')
