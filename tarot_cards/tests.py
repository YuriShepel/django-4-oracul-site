from http import HTTPStatus

from django.test import TestCase, TransactionTestCase
from django.urls import reverse

from common_segments.common.mixins import TarotSetUpTestMixin
from tarot_cards.models import Card


class TarotSuitListViewTestCase(TarotSetUpTestMixin, TestCase):

    def test_tarot_suits_list_view_status_code(self):
        path = reverse('tarot_cards:tarot_suits')
        self.response = self.client.get(path)
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertIn('major_arcana', self.response.context)
        self.assertIn('minor_arcana', self.response.context)
        self.assertEqual(self.response.context['major_arcana'], self.suit)


class CardsListViewTestCase(TarotSetUpTestMixin, TransactionTestCase):

    def test_cards_list_view_status_code(self):
        path = reverse('tarot_cards:cards_list', kwargs={'slug': 'test-suit'})
        self.response = self.client.get(path)
        self.assertEqual(self.response.status_code, HTTPStatus.OK)


class TarotSuitDetailViewTestCase(TarotSetUpTestMixin, TransactionTestCase):
    def setUp(self):
        super(TarotSuitDetailViewTestCase, self).setUp()
        self.response = self.client.get(f'/tarot_cards/suit_description/{self.suit.url}/')

    def test_tarot_suit_detail_view_status_code(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)

    def test_tarot_suit_detail_view_template_name(self):
        self.assertTemplateUsed(self.response, 'tarot_cards/tarot_suit_detail.html')

    def test_tarot_suit_detail_view_content(self):
        self.assertIn('test_description', self.response.content.decode())


class TarotCardDetailViewTestCase(TarotSetUpTestMixin, TransactionTestCase):
    def setUp(self):
        super(TarotCardDetailViewTestCase, self).setUp()
        self.card = Card.objects.create(
            name='test_suit',
            general_meaning='test_text',
            image_1='static/images/tarot_img/cups/2_cups.png',
            url='test-suit',
            card_suit=self.suit
        )
        self.response = self.client.get(f'/tarot_cards/{self.card.url}/')

    def test_card_detail_view_status_code(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)

    def test_card_detail_view_template_name(self):
        self.assertTemplateUsed(self.response, 'tarot_cards/card_detail.html')

    def test_card_detail_view_content(self):
        self.assertIn('test_text', self.response.content.decode())
