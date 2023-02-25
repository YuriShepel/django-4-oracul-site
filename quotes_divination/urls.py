from django.urls import path

from . import views

app_name = 'quotes_divination'


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_quotes_list'),
    path('<slug:slug>/', views.RandomQuoteView.as_view(), name='random_quote'),
]