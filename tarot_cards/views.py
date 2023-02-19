from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views import View

from common.views import TitleMixin
from .models import TarotSuits, Card


class IndexView(TitleMixin, TemplateView):
    """Displaying the home page of the site"""
    template_name = 'tarot_cards/index.html'
    title = 'Гадания онлайн'


class TarotSuitView(TitleMixin, TemplateView):
    """Displaying the page with all suits"""
    template_name = 'tarot_cards/tarot_suits.html'
    title = 'Справочник таро'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        major_arcana = TarotSuits.objects.get(id=1)
        minor_arcana = TarotSuits.objects.filter(id__range=(2, 5))
        context['major_arcana'] = major_arcana
        context['minor_arcana'] = minor_arcana
        return context


class CardsView(View):
    def get(self, request, suit_slug):
        suit = get_object_or_404(TarotSuits, url=suit_slug)
        cards = Card.objects.filter(card_suit=suit).order_by('id')
        context = {
            'cards': cards,
            'suit': suit,
        }
        return render(request, 'tarot_cards/cards_list.html', context)


class SuitDescriptionView(View):
    def get(self, request, suit_slug):
        suit = get_object_or_404(TarotSuits, url=suit_slug)
        return render(request, 'tarot_cards/suit_description.html', {'suit': suit})


class CardDetailView(DetailView):
    """Displaying detail information of the card"""
    model = Card
    template_name = 'tarot_cards/card_detail.html'
    context_object_name = 'card'
    slug_field = 'url'
    slug_url_kwarg = 'card_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = context['card']
        context['image_2'] = card.card_suit.image_2
        return context
