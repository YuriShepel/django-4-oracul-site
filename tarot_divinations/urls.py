from django.urls import path

from . import views

app_name = 'tarot_devinations'


urlpatterns = [
    path('', views.TarotDayCardView.as_view(), name='tarot_day_card_view'),
    path('card-of-the-day/', views.CardOfDayView.as_view(), name='card_of_the_day')
    # path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail')
]
