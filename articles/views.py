from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Article


class ArticlesView(ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'articles/articles.html'


class ArticleDitailDetail(DetailView):
    model = Article
    slug_field = 'url'

