from django.urls import path

from . import views

app_name = 'articles'


urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles_view'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail')
]
