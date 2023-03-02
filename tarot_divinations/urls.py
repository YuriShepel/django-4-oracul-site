from django.urls import path

from . import views

app_name = 'tarot_devinations'


urlpatterns = [
    path('card_of_the_day_divination/', views.TarotDayCardView.as_view(), name='tarot_day_card_view'),
    path('card-of-the-day/', views.CardOfDayView.as_view(), name='card_of_the_day'),
    path('three_tarot_cards_divination/', views.TarotThreeCardsView.as_view(), name='tarot_three_cards_view'),
    path('three_tarot_cards/', views.ThreeTarotCardsList.as_view(), name='three_tarot_cards'),
    path('yes_or_no_tarot_divination/', views.YesOrNoTarotView.as_view(), name='yes_or_no_tarot_view'),
    path('yes_or_no_tarot/', views.YesOrNoTarotDetail.as_view(), name='yes_or_no_tarot'),
]
