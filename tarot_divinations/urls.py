from django.urls import path

from . import views

app_name = 'tarot_devinations'


urlpatterns = [
    path('', views.TarotDayCardView.as_view(), name='tarot_day_card_view'),
    path('card-of-the-day/', views.CardOfDayView.as_view(), name='card_of_the_day'),
    path('three_tarot_cards_divination/', views.TarotThreeCardsView.as_view(), name='tarot_three_cards_view'),
    path('three_tarot_cards/', views.three_tarot_cards, name='three_tarot_cards'),
]
