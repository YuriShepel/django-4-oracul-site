from django.urls import path

from . import views

app_name = 'person_characteristic'

urlpatterns = [

    path('birthday-description/', views.WeekDayDescriptionView.as_view(), name='birthday'),
    path('birthday-description/<slug:slug>/', views.WeekDayDescriptionDetailView.as_view(), name='day_detail'),
    path('color-description/', views.ColorDescriptionListView.as_view(), name='color_description'),
    path('color-description/<slug:slug>/', views.ColorDescriptionDetailView.as_view(), name='color_detail'),
    path('month-day-description/', views.MonthDayDescriptionListView.as_view(), name='month_day_description'),
    path('month-day-description/<slug:slug>/', views.MonthDayDescriptionDetailView.as_view(), name='month_day_detail'),

]
