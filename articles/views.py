from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404

from . models import Article


def articles_view(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles})


def article_detail(request, article_slug):
    article = Article.objects.get(url=article_slug)
    return render(request, 'articles/article_detail.html', {'article': article})
