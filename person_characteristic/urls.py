from django.urls import path

from . import views

app_name = 'person_characteristic'

urlpatterns = [

    path('birthday_description/', views.WeekDayDescriptionView.as_view(), name='birthday'),
    path('birthday_description/<slug:slug>/', views.WeekDayDescriptionDetailView.as_view(), name='day_detail'),
    path('color_description/', views.ColorDescriptionListView.as_view(), name='color_description'),
    path('color_description/<slug:slug>/', views.ColorDescriptionDetailView.as_view(), name='color_detail'),
    path('month_day_description/', views.MonthDayDescriptionListView.as_view(), name='month_day_description'),

]
