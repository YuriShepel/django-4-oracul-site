from django.contrib.sitemaps import Sitemap

from articles.models import Article
from person_characteristic.models import (ColorCharacter, MonthDayCharacter,
                                          WeekDayCharacter)
from tarot_cards.models import Card, TarotSuits


class BaseStaticSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'


class StaticPagesSitemap(BaseStaticSitemap):
    # Создаем словарь соответствия между элементами и их местоположениями
    ITEM_LOCATIONS = {
        'index': '/',
        'about': '/about/',
        'contacts': '/contacts/',
        'privacy_policy': '/privacy-policy/',
        'tarot_day_card_view': '/tarot-divinations/card-of-the-day-divination/',
        'love_situation_tarot_view': '/tarot-divinations/love-situation-tarot-divination/',
        'career_situation_tarot_view': '/tarot-divinations/career-situation-tarot-divination/',
        'finance_situation_tarot_view': '/tarot-divinations/finance-situation-tarot-divination/',
        'yes_or_no_tarot_view': '/tarot-divinations/yes-or-no-tarot-divination/',
        'tarot_three_cards_view': '/tarot-divinations/three-tarot-cards-divination/',
        'category_quotes_list': '/quotes-divination/',

        'color_description': '/person/color-description/',
        'birthday': '/person/birthday-description/',
        'month_day_description': '/person/month-day-description/',

        'tarot_suits': '/tarot-cards/tarot-suits/',
    }

    def items(self):
        # Возвращаем список всех элементов
        return list(self.ITEM_LOCATIONS.keys())

    def location(self, obj):
        # Используем словарь для получения местоположения элемента
        return self.ITEM_LOCATIONS[obj]


class ArticleSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return Article.objects.filter(moderation=True)

    def location(self, obj):
        return f'/articles/{obj.url}/'


class SuitDescriptionSitemap(BaseStaticSitemap):
    def items(self):
        return TarotSuits.objects.all()

    def location(self, obj):
        return f'/tarot-cards/suit-description/{obj.url}/'


class TarotCardSitemap(BaseStaticSitemap):

    def items(self):
        return Card.objects.all()

    def location(self, obj):
        return f'/tarot-cards/{obj.url}/'


class ColorCharacterSitemap(BaseStaticSitemap):

    def items(self):
        return ColorCharacter.objects.all()

    def location(self, obj):
        return f'/person/color-description/{obj.url}/'


class BirthdayDescriptionSitemap(BaseStaticSitemap):

    def items(self):
        return WeekDayCharacter.objects.all()

    def location(self, obj):
        return f'/person/birthday-description/{obj.url}/'


class MonthDayDescriptionSitemap(BaseStaticSitemap):

    def items(self):
        return MonthDayCharacter.objects.all()

    def location(self, obj):
        return f'/person/month-day-description/{obj.url}/'
