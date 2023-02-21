from django.views.generic import DetailView, ListView

from .models import Article


class ArticlesListView(ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'articles/articles.html'


class ArticleDetailView(DetailView):
    model = Article
    slug_field = 'url'
