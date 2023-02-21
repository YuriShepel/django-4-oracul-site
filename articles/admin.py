from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import Article, Category


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'moderation')
    list_filter = ('categories', 'created', 'moderation')
    search_fields = ('title', 'categories__name', 'description')
    form = ArticleAdminForm

    date_hierarchy = 'created'

    filter_vertical = ('categories',)

    fieldsets = (
        ('Основные параметры', {
            'fields': ('title', 'image', 'description', 'text', 'categories'), 'classes': ['wide']
        }),
        ('SEO', {
            'fields': ('seo_description', 'seo_keywords'), 'classes': ['wide']
        }),
        ('Дополнительные параметры', {
            'fields': ('url', 'created', 'moderation'), 'classes': ['wide']
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')

    fieldsets = (
        ('Основные параметры', {
            'fields': ('name', 'description', 'url'), 'classes': ['wide']
        }),
    )
