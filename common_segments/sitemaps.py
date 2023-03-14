from django.contrib.sitemaps import Sitemap

from articles.models import Article
from person_characteristic.models import ColorCharacter, WeekDayCharacter, MonthDayCharacter
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
        'privacy_policy': '/privacy_policy/',
        'tarot_day_card_view': '/tarot_divinations/card_of_the_day_divination/',
        'love_situation_tarot_view': '/tarot_divinations/love_situation_tarot_divination/',
        'career_situation_tarot_view': '/tarot_divinations/career_situation_tarot_divination/',
        'finance_situation_tarot_view': '/tarot_divinations/finance_situation_tarot_divination/',
        'yes_or_no_tarot_view': '/tarot_divinations/yes_or_no_tarot_divination/',
        'tarot_three_cards_view': '/tarot_divinations/three_tarot_cards_divination/',
        'category_quotes_list': '/quotes_divination/',

        'color_description': '/person/color_description/',
        'birthday': '/person/birthday_description/',
        'month_day_description': '/person/month_day_description/',

        'tarot_suits': '/tarot_cards/tarot_suits/',
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
        return f'/tarot_cards/suit_description/{obj.url}/'


class TarotCardSitemap(BaseStaticSitemap):

    def items(self):
        return Card.objects.all()

    def location(self, obj):
        return f'/tarot_cards/{obj.url}/'


class ColorCharacterSitemap(BaseStaticSitemap):

    def items(self):
        return ColorCharacter.objects.all()

    def location(self, obj):
        return f'/person/color_description/{obj.url}/'


class BirthdayDescriptionSitemap(BaseStaticSitemap):

    def items(self):
        return WeekDayCharacter.objects.all()

    def location(self, obj):
        return f'/person/birthday_description/{obj.url}/'


class MonthDayDescriptionSitemap(BaseStaticSitemap):

    def items(self):
        return MonthDayCharacter.objects.all()

    def location(self, obj):
        return f'/person/month_day_description/{obj.url}/'
