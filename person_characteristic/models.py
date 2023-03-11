from django.db import models


class BaseCharacter(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color_code = models.CharField(max_length=20, null=True)
    text = models.TextField()
    url = models.SlugField(max_length=100, unique=True)
    seo_description = models.TextField(null=True, blank=True)
    seo_keywords = models.CharField(max_length=300, null=True, blank=True)
    moderation = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name} | {self.moderation}'


class ColorCharacter(BaseCharacter):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class WeekDayCharacter(BaseCharacter):
    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class MonthDayCharacter(BaseCharacter):
    class Meta:
        verbose_name = 'День месяца'
        verbose_name_plural = 'Дни месяца'
