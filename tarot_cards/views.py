from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from .models import TarotSuits, Card


def base_view(request):
    names = TarotSuits.objects.values_list('suits_name', flat=True)
    return render(request, 'tarot_cards/base.html', {'names': names})


class IndexView(TitleMixin, TemplateView):
    """Displaying the home page of the site"""
    template_name = 'tarot_cards/index.html'
    title = 'Гадания онлайн'


def tarot_suit_view(request):
    cards = [('major', 'Старшие арканы'), ('cups', 'Кубки'), ('wands', 'Жезлы'), ('pentacles', 'Пентакли'),
             ('swords', 'Мечи')]
    context = {k: TarotSuits.objects.get(suits_name=v) for k, v in cards}
    return render(request, 'tarot_cards/tarot_suits.html', context)


def cards_list(request, suit_slug):
    suit = get_object_or_404(TarotSuits, url=suit_slug)
    image = suit.image_1
    title = suit.suits_name
    cards = Card.objects.filter(card_suit=suit)
    context = {
        'cards': cards,
        'title': title,
        'image': image,
        'suit': suit
    }
    return render(request, 'tarot_cards/cards_list.html', context)
