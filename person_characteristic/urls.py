from django.urls import path

from . import views

app_name = 'person_characteristic'

urlpatterns = [

    path('birthday/', views.WeekDayDescriptionView.as_view(), name='birthday'),
    path('color_description/', views.ColorDescriptionListView.as_view(), name='color_description'),
    path('<slug:slug>/', views.ColorDescriptionDetailView.as_view(), name='color_detail'),

]
