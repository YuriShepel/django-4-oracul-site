import random

from django.views.generic import TemplateView, DetailView

from random import randint, sample
from django.shortcuts import render
from tarot_cards.models import Card

from common_segments.common.mixins import TitleMixin


class TarotDayCardView(TitleMixin, TemplateView):
    """Displaying """
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
        context['name'] = self.object.name
        context['day_card_text'] = self.object.card_of_day
        context['image'] = self.object.image_1
        context['day_card_advice'] = self.object.card_advice
        return context


class TarotThreeCardsView(TitleMixin, TemplateView):
    """"""
    template_name = 'tarot_devinations/tarot_three_cards_view.html'
    title = 'Онлайн гадание Три Карты'


# def three_tarot_cards(request):
#     # Получить три случайных карты
#     cards = sample(list(Card.objects.all()), 3)
#
#     # Создать список, содержащий данные для каждой карты
#     cards_data = []
#     for card in cards:
#         cards_data.append({
#             'name': card.name,
#             'image': card.image_1,
#             'meaning': card.past_meaning if card == cards[0]
#             else card.present_meaning if card == cards[1]
#             else card.future_meaning
#         })
#
#     # Отображение результатов
#     return render(request, 'tarot_devinations/tarot_three_cards_detail.html', {'cards_data': cards_data})
def three_tarot_cards(request):
    # Получить три случайных карты
    cards = sample(list(Card.objects.all()), 3)

    # Создать список, содержащий данные для каждой карты
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

    # Отображение результатов
    return render(request, 'tarot_devinations/tarot_three_cards_detail.html', {'cards_data': cards_data})
