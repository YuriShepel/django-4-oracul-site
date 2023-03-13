from django.contrib.sitemaps import Sitemap

from articles.models import Article
from person_characteristic.models import ColorCharacter, WeekDayCharacter, MonthDayCharacter
from tarot_cards.models import Card


class BaseStaticSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'


class ArticleSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return Article.objects.filter(moderation=True)

    def location(self, obj):
        return f'/articles/{obj.url}/'


class TarotCardSitemap(BaseStaticSitemap):

    def items(self):
        return Card.objects.all()

    def location(self, obj):
        return f'/tarot_cards/{obj.url}/'


class CardOfTheDayDivinationSitemap(BaseStaticSitemap):

    def items(self):
        return ['tarot_day_card_view']

    def location(self, item):
        return '/tarot_divinations/card_of_the_day_divination/'


class LoveSituationTarotDivinationSitemap(BaseStaticSitemap):

    def items(self):
        return ['love_situation_tarot_view']

    def location(self, item):
        return '/tarot_divinations/love_situation_tarot_divination/'


class CareerSituationTarotDivinationSitemap(BaseStaticSitemap):

    def items(self):
        return ['career_situation_tarot_view']

    def location(self, item):
        return '/tarot_divinations/career_situation_tarot_divination/'


class FinanceSituationTarotDivinationSitemap(BaseStaticSitemap):

    def items(self):
        return ['finance_situation_tarot_view']

    def location(self, item):
        return '/tarot_divinations/finance_situation_tarot_divination/'


class YesOrNoTarotDivinationSitemap(BaseStaticSitemap):

    def items(self):
        return ['yes_or_no_tarot_view']

    def location(self, item):
        return '/tarot_divinations/yes_or_no_tarot_divination/'


class ColorCharacterSitemap(BaseStaticSitemap):

    def items(self):
        return ColorCharacter.objects.all()

    def location(self, obj):
        return f'/person/color_description/{obj.url}/'


class ColorCharacterViewSitemap(BaseStaticSitemap):

    def items(self):
        return ['color_description']

    def location(self, obj):
        return f'/person/color_description/'


class BirthdayDescriptionSitemap(BaseStaticSitemap):

    def items(self):
        return WeekDayCharacter.objects.all()

    def location(self, obj):
        return f'/person/birthday_description/{obj.url}/'


class BirthdayDescriptionViewSitemap(BaseStaticSitemap):

    def items(self):
        return ['birthday']

    def location(self, obj):
        return f'/person/birthday_description/'


class MonthDayDescriptionSitemap(BaseStaticSitemap):

    def items(self):
        return MonthDayCharacter.objects.all()

    def location(self, obj):
        return f'/person/month_day_description/{obj.url}/'


class MonthDayDescriptionViewSitemap(BaseStaticSitemap):

    def items(self):
        return ['month_day_description']

    def location(self, obj):
        return f'/person/month_day_description/'
