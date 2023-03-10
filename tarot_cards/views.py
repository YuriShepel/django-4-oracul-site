from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.list import ListView

from common_segments.common.mixins import TitleMixin

from .models import Card, TarotSuits


class TarotSuitListView(TitleMixin, ListView):
    """Displays all suits page"""
    model = TarotSuits
    title = 'Справочник таро'
    template_name = 'tarot_cards/tarot_suits.html'
    context_object_name = 'suits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['major_arcana'] = TarotSuits.objects.get(id=1)
        context['minor_arcana'] = TarotSuits.objects.filter(id__range=(2, 5))
        return context


class CardsListView(ListView):
    """Displays cards of a specified suit"""
    model = Card
    template_name = 'tarot_cards/cards_list.html'
    context_object_name = 'cards'

    def get_queryset(self):
        suit = get_object_or_404(TarotSuits, url=self.kwargs['slug'])
        return Card.objects.filter(card_suit=suit).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        suit = get_object_or_404(TarotSuits, url=self.kwargs['slug'])
        context['suit'] = suit
        return context


class TarotSuitDetailView(DetailView):
    """Displays suit detail page"""
    model = TarotSuits
    template_name = 'tarot_cards/tarot_suit_detail.html'
    context_object_name = 'suit'
    slug_field = 'url'


class CardDetailView(DetailView):
    """Displays card detail page"""
    model = Card
    slug_field = 'url'
