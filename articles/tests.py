from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from articles.models import Article, Category


class ArticlesListViewTestCase(TestCase):

    def setUp(self):
        path = reverse('articles:articles_view')
        self.response = self.client.get(path)

    def test_articles_list_view_status_code(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)

    def test_articles_list_view_template_name(self):
        self.assertTemplateUsed(self.response, 'articles/articles.html')

    def test_articles_list_view_title_name(self):
        self.assertEqual(self.response.context_data['title'], 'Статьи о Таро и гаданиях')

    #
    def test_index_view_content(self):
        self.assertIn('Интересные статьи', self.response.content.decode())


class ArticleDetailViewTestCase(TestCase):
    def setUp(self):
        test_category = Category.objects.create(name="Test Category")
        self.article = Article.objects.create(
            title='My article title',
            text='My article content',
            url='my-article-slug',
            created=timezone.now()
        )
        self.article.categories.add(test_category)
        self.response = self.client.get(f'/articles/{self.article.url}/')

    def test_article_detail_view_status_code(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)

    def test_articles_detail_view_template_name(self):
        self.assertTemplateUsed(self.response, 'articles/article_detail.html')

    def test_index_view_content(self):
        self.assertIn('My article content', self.response.content.decode())
