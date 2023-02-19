from django.urls import path

from . import views

app_name = 'tarot_cards'

# cards_list_template = 'tarot_cards/cards_list.html'
# suit_description_template = 'tarot_cards/suit_description.html'

urlpatterns = [
    path('tarot_suits/', views.TarotSuitView.as_view(), name='tarot_suits'),
    path('tarot_suits/<slug:suit_slug>/', views.CardsView.as_view(), name='cards_list'),
    path('suit_description/<slug:suit_slug>/', views.SuitDescriptionView.as_view(), name='suit_description'),
    path('<slug:card_slug>/', views.CardDetailView.as_view(), name='card_detail'),
]
