from django.db import models


class ColorCharacter(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color_code = models.CharField(max_length=20, unique=True)
    text = models.TextField()

    url = models.SlugField(max_length=100, unique=True)

    seo_description = models.TextField(null=True, blank=True)
    seo_keywords = models.CharField(max_length=300, null=True, blank=True)

    moderation = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return f'{self.name} | {self.moderation}'
