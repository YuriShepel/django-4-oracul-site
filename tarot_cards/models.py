from django.db import models


class TarotSuits(models.Model):
    suits_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    positive_description = models.TextField(null=True, blank=True)
    negative_description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    astrological_signs = models.CharField(max_length=255, null=True, blank=True)
    alternative_names = models.CharField(max_length=255, null=True, blank=True)

    image_1 = models.ImageField(upload_to='tarot_cards/suits_images', blank=True)
    image_2 = models.ImageField(upload_to='tarot_cards/suits_images', blank=True)
    image_3 = models.ImageField(upload_to='tarot_cards/suits_images', blank=True)
    image_4 = models.ImageField(upload_to='tarot_cards/suits_images', blank=True)

    seo_description = models.TextField(null=True, blank=True)
    seo_tags = models.CharField(max_length=255, unique=True, null=True, blank=True)

    url = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Масть таро'
        verbose_name_plural = 'Масти таро'

    def __str__(self):
        return self.suits_name


class Card(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_1 = models.ImageField(upload_to='tarot_cards/cards_images', blank=True)

    general_up_tags = models.TextField(null=True, blank=True)
    general_down_tags = models.TextField(null=True, blank=True)
    general_meaning = models.TextField(null=True, blank=True)
    general_up = models.TextField(null=True, blank=True)
    general_down = models.TextField(null=True, blank=True)

    love_up_tags = models.TextField(null=True, blank=True)
    love_down_tags = models.TextField(null=True, blank=True)
    love_up = models.TextField(null=True, blank=True)
    love_down = models.TextField(null=True, blank=True)

    career_up_tags = models.TextField(null=True, blank=True)
    career_down_tags = models.TextField(null=True, blank=True)
    career_up = models.TextField(null=True, blank=True)
    career_down = models.TextField(null=True, blank=True)

    finance_up_tags = models.TextField(null=True, blank=True)
    finance_down_tags = models.TextField(null=True, blank=True)
    finance_up = models.TextField(null=True, blank=True)
    finance_down = models.TextField(null=True, blank=True)

    past_meaning = models.TextField(null=True, blank=True)
    present_meaning = models.TextField(null=True, blank=True)
    future_meaning = models.TextField(null=True, blank=True)

    card_of_day = models.TextField(null=True, blank=True)
    card_advice = models.TextField(null=True, blank=True)

    yes_no = models.CharField(max_length=255, null=True, blank=True)

    card_suit = models.ForeignKey(to=TarotSuits, on_delete=models.CASCADE)

    seo_description = models.TextField(null=True, blank=True)
    seo_key_words = models.CharField(max_length=255, null=True, blank=True)

    url = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return f'{self.name} ------- {self.card_suit}'
