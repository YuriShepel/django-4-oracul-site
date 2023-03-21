from django.urls import path

from . import views

app_name = 'tarot_devinations'

urlpatterns = [
    path('card-of-the-day-divination/', views.TarotDayCardView.as_view(), name='tarot_day_card_view'),
    path('card-of-the-day/', views.CardOfDayView.as_view(), name='card_of_the_day'),
    path('three-tarot-cards-divination/', views.TarotThreeCardsView.as_view(), name='tarot_three_cards_view'),
    path('three-tarot-cards/', views.ThreeTarotCardsList.as_view(), name='three_tarot_cards'),
    path('yes-or-no-tarot-divination/', views.YesOrNoTarotView.as_view(), name='yes_or_no_tarot_view'),
    path('yes-or-no-tarot/', views.YesOrNoTarotDetail.as_view(), name='yes_or_no_tarot'),
    path('love-situation-tarot-divination/', views.LoveSituationTarotView.as_view(), name='love_situation_tarot_view'),
    path('love-situation-tarot/', views.LoveSituationTarotDetail.as_view(), name='love_situation_tarot'),
    path('career-situation-tarot-divination/', views.CareerSituationTarotView.as_view(),
         name='career_situation_tarot_view'),
    path('career-situation-tarot/', views.CareerSituationTarotDetail.as_view(), name='career_situation_tarot'),
    path('finance-situation-tarot-divination/', views.FinanceSituationTarotView.as_view(),
         name='finance_situation_tarot_view'),
    path('finance-situation-tarot/', views.FinanceSituationTarotDetail.as_view(), name='finance_situation_tarot'),
]
