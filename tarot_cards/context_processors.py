import random

from articles.models import Article


def right_sidebar(request):
    articles = Article.objects.all()
    random_articles = random.sample(list(articles), 3)
    return {'right_sidebar_articles': random_articles}
