from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    url = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория статьи'
        verbose_name_plural = 'Категории статьи'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=300, unique=True)
    image = models.ImageField(upload_to='articles/articles_images', blank=True)
    description = models.CharField(max_length=300, blank=True)
    text = models.TextField()
    categories = models.ManyToManyField(Category)

    url = models.SlugField(max_length=100, unique=True)

    seo_description = models.TextField(null=True, blank=True)
    seo_keywords = models.CharField(max_length=300, null=True, blank=True)

    created = models.DateTimeField()

    moderation = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.title} | {self.categories} | {self.created}'
