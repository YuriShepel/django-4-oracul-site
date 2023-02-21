from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class IndexViewTestCase(TestCase):

    def setUp(self):
        path = reverse('index')
        self.response = self.client.get(path)

    def test_index_view_status_code(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)

    def test_index_view_template_name(self):
        self.assertTemplateUsed(self.response, 'common_segments/index.html')

    def test_index_view_title_name(self):
        self.assertEqual(self.response.context_data['title'], 'Гадания онлайн')

    def test_index_view_content(self):
        self.assertIn('Добро пожаловать в мир гаданий и карт Таро!', self.response.content.decode())
