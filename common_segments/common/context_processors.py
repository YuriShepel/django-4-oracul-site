from django.db.models.functions import Random

from articles.models import Article


def right_sidebar(request):
    random_articles = Article.objects.annotate(random_number=Random()).order_by('random_number')[:4]
    return {'right_sidebar_articles': random_articles}

# import random
#
# from articles.models import Article
#
#
# def right_sidebar(request):
#     articles = Article.objects.all()
#     random_articles = random.sample(list(articles), 4)
#     return {'right_sidebar_articles': random_articles}
