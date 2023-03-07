from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = 'tarot_cards'

urlpatterns = [
    path('tarot_suits/', cache_page(30)(views.TarotSuitListView.as_view()), name='tarot_suits'),
    path('tarot_suits/<slug:slug>/', cache_page(30)(views.CardsListView.as_view()), name='cards_list'),
    path('suit_description/<slug:slug>/', cache_page(30)(views.TarotSuitDetailView.as_view()), name='suit_description'),
    path('<slug:slug>/', cache_page(30)(views.CardDetailView.as_view()), name='card_detail'),
]
