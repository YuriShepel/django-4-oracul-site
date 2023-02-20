from django.urls import path

from . import views

app_name = 'articles'


urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles_view'),
    path('<slug:slug>/', views.ArticleDitailDetail.as_view(), name='article_detail')
]