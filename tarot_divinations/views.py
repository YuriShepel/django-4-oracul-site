from django.views.generic import TemplateView, DetailView

from random import randint
from django.shortcuts import render
from tarot_cards.models import Card

from common_segments.common.mixins import TitleMixin


class TarotDayCardView(TitleMixin, TemplateView):
    """Displaying the home page of the site"""
    template_name = 'tarot_devinations/tarot_day_card_view.html'
    title = 'Онлайн гадание Карта Дня Таро'


class CardOfDayView(DetailView):
    model = Card
    template_name = 'tarot_devinations/tarot_day_card_detail.html'

    def get_object(self, queryset=None):
        count = self.get_queryset().count()
        random_index = randint(0, count - 1)
        return super().get_queryset().all()[random_index]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['day_card_text'] = self.object.card_of_day
        context['image'] = self.object.image_1
        context['day_card_advice'] = self.object.card_advice
        return context

