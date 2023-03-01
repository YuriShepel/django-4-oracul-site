import random

from django.views.generic import TemplateView, DetailView

from random import sample
from django.shortcuts import render
from tarot_cards.models import Card
from django.views.generic.list import ListView
from common_segments.common.mixins import TitleMixin


class TarotDayCardView(TitleMixin, TemplateView):
    """Displaying """
    template_name = 'tarot_devinations/tarot_day_card_view.html'
    title = 'Онлайн гадание Карта Дня Таро'


class CardOfDayView(DetailView):
    model = Card
    template_name = 'tarot_devinations/tarot_day_card_detail.html'

    def get_object(self, queryset=None):
        return self.get_queryset().order_by('?').first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.object.name
        context['image'] = self.object.image_1
        context['day_card_text'] = self.object.card_of_day
        context['day_card_advice'] = self.object.card_advice
        return context


class TarotThreeCardsView(TitleMixin, TemplateView):
    """"""
    template_name = 'tarot_devinations/tarot_three_cards_view.html'
    title = 'Онлайн гадание Три Карты'


class ThreeTarotCardsList(ListView):
    template_name = 'tarot_devinations/tarot_three_cards_detail.html'
    model = Card

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cards = sample(list(self.model.objects.all()), 3)
        cards_data = []
        periods = ['Прошлое', 'Настоящее', 'Будущее']
        for i, card in enumerate(cards):
            cards_data.append({
                'name': card.name,
                'image': card.image_1,
                'meaning': card.past_meaning if i == 0
                else card.present_meaning if i == 1
                else card.future_meaning,
                'period': periods[i],
            })
        context['cards_data'] = cards_data
        return context

