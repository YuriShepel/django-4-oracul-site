from django.core.paginator import EmptyPage, Paginator
from django.views.generic import DetailView, ListView

from common_segments.common.mixins import TitleMixin

from .models import Article


class ArticlesListView(TitleMixin, ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'articles/articles.html'
    title = 'Статьи о Таро и гаданиях'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')
        if page and page.isnumeric():
            page = int(page)
        else:
            page = 1

        try:
            articles = paginator.page(page)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        context['articles'] = articles
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    slug_field = 'url'
