from django.views.generic import DetailView, ListView

from common_segments.common.mixins import TitleMixin
from .models import Article


class ArticlesListView(TitleMixin, ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'articles/articles.html'
    title = 'Статьи о Таро и гаданиях'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    slug_field = 'url'
