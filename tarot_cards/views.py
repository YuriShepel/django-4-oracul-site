from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'tarot_cards/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Гадания онлайн'
        return context


class TarotSuitsView(TemplateView):
    template_name = 'tarot_cards/tarot_suits.html'

    def get_context_data(self, **kwargs):
        context = super(TarotSuitsView, self).get_context_data()
        context['title'] = 'Масти таро'
        return context
