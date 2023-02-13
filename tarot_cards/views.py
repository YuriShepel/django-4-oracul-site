from django.shortcuts import render
from django.views.generic.base import TemplateView

from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'tarot_cards/index.html'
    title = 'Гадания онлайн'


class TarotSuitsView(TitleMixin, TemplateView):
    template_name = 'tarot_cards/tarot_suits.html'
    title = 'Масти таро'

