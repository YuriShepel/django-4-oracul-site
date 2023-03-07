from random import sample

from django.views.generic import DetailView, TemplateView
from django.views.generic.list import ListView

from common_segments.common.mixins import TitleMixin, TarotMixin
from tarot_cards.models import Card


class TarotDayCardView(TitleMixin, TemplateView):
    """Displays the welcome text of the Tarot Card of the Day"""
    template_name = 'tarot_devinations/tarot_day_card_view.html'
    title = 'Онлайн гадание Карта Дня Таро'


class CardOfDayView(TarotMixin, DetailView):
    """Displays the Tarot card of the day"""
    template_name = 'tarot_devinations/tarot_day_card_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['day_card_text'] = self.object.card_of_day
        context['day_card_advice'] = self.object.card_advice
        return context


class TarotThreeCardsView(TitleMixin, TemplateView):
    """Displays the welcome text of the Three Tarot card divination"""
    template_name = 'tarot_devinations/tarot_three_cards_view.html'
    title = 'Онлайн гадание Три Карты'


class ThreeTarotCardsList(ListView):
    """Displays three Tarot cards"""
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


class YesOrNoTarotView(TitleMixin, TemplateView):
    """Displays the welcome text of the Yes or No divination"""
    template_name = 'tarot_devinations/yes_or_no_card_view.html'
    title = 'Онлайн гадание Да или Нет'


class YesOrNoTarotDetail(TarotMixin, DetailView):
    """Displays Yes or No divination"""
    template_name = 'tarot_devinations/yes_or_no_card_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['yes_or_no'] = self.object.yes_no
        return context


class LoveSituationTarotView(TitleMixin, TemplateView):
    """Displays the welcome text of the Love Situation divination"""
    template_name = 'tarot_devinations/tarot_love_situation_view.html'
    title = 'Онлайн гадание Любовная ситуация'


class LoveSituationTarotDetail(TarotMixin, DetailView):
    """Displays Love Situation divination"""
    template_name = 'tarot_devinations/tarot_love_situation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['love_up'] = self.object.love_up
        context['love_down'] = self.object.love_down
        return context


class CareerSituationTarotView(TitleMixin, TemplateView):
    """Displays the welcome text of the Love Situation divination"""
    template_name = 'tarot_devinations/tarot_career_situation_view.html'
    title = 'Онлайн гадание Ситуация на работе'


class CareerSituationTarotDetail(TarotMixin, DetailView):
    """Displays Love Situation divination"""
    template_name = 'tarot_devinations/tarot_career_situation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['career_up'] = self.object.career_up
        context['career_down'] = self.object.career_down
        return context
