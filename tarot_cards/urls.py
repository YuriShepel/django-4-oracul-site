from django.urls import path

from . import views

app_name = 'tarot_cards'

urlpatterns = [
    path('tarot_suits/', views.tarot_suit_view, name='tarot_suits'),
    path('tarot_suits/<slug:suit_slug>', views.cards_list, name='cards_list'),
]
