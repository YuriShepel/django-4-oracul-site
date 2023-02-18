from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views import View

from common.views import TitleMixin
from .models import TarotSuits, Card


class IndexView(TitleMixin, TemplateView):
    """Displaying the home page of the site"""
    template_name = 'tarot_cards/index.html'
    title = 'Гадания онлайн'


def tarot_suit_view(request):
    major_arcana = TarotSuits.objects.get(id=1)
    minor_arcana = TarotSuits.objects.filter(id__range=(2, 5))

    context = {
        'title': 'Справочник таро',
        'major_arcana': major_arcana,
        'minor_arcana': minor_arcana
    }
    return render(request, 'tarot_cards/tarot_suits.html', context)


class CardsAndSuitsView(View):
    cards_list_template = 'tarot_cards/cards_list.html'
    suit_description_template = 'tarot_cards/suit_description.html'

    def get(self, request, suit_slug):
        suit = get_object_or_404(TarotSuits, url=suit_slug)
        if self.cards_list_template:
            cards = Card.objects.filter(card_suit=suit).order_by('id')
            context = {
                'cards': cards,
                'suit': suit,
            }
            return render(request, 'tarot_cards/cards_list.html', context)
        if self.suit_description_template:
            return render(request, 'tarot_cards/suit_description.html', {'suit': suit})


def card_detail_view(request, card_slug):
    card = get_object_or_404(Card, url=card_slug)
    image_2 = card.card_suit.image_2
    context = {
        'card': card,
        'image_2': image_2
    }
    return render(request, 'tarot_cards/card_detail.html', context)
