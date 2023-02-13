from django.urls import path

from . import views

app_name = 'tarot_cards'

urlpatterns = [
    path('', views.TarotSuitsView.as_view(), name='tarot_suits'),
]