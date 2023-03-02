from django.contrib import admin

from .models import Category, Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('category', 'author')
    list_filter = ('category', 'author')
    search_fields = ('category', 'author')

    fieldsets = (
        ('Основные параметры', {
            'fields': ('category', 'author', 'quote'), 'classes': ['wide']
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

    fieldsets = (
        ('Основные параметры', {
            'fields': ('name', 'url', 'image'), 'classes': ['wide']
        }),
    )
