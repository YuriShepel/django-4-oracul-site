from django.db import models


class Category(models.Model):
    name = models.CharField('Категории', max_length=100)
    url = models.SlugField('Ссылка', max_length=100)
    image = models.ImageField(upload_to='quotes/quotes_images', blank=True, null=True, default=None)
    image_alt = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории цитат'
        verbose_name_plural = 'Категории цитат'


class Quote(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    author = models.CharField('Автор', max_length=100)
    quote = models.TextField()

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
