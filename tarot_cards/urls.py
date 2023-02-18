from django.urls import path

from . import views

app_name = 'tarot_cards'

cards_list_template = 'tarot_cards/cards_list.html'
suit_description_template = 'tarot_cards/suit_description.html'

urlpatterns = [
    path('tarot_suits/', views.tarot_suit_view, name='tarot_suits'),
    path('tarot_suits/<slug:suit_slug>/',
         views.CardsAndSuitsView.as_view(cards_list_template=cards_list_template, suit_description_template=None),
         name='cards_list'),
    path('suit_description/<slug:suit_slug>/',
         views.CardsAndSuitsView.as_view(cards_list_template=None, suit_description_template=suit_description_template),
         name='suit_description'),
    path('<slug:card_slug>/', views.card_detail_view, name='card_detail'),
]
