from django.contrib import admin

from .models import TarotSuits, Card


@admin.register(TarotSuits)
class TarotSuitsAdmin(admin.ModelAdmin):
    list_display = ('suits_name', 'url',)
    list_filter = ('astrological_signs',)
    search_fields = ('suits_name', 'keywords',)

    fieldsets = (
        ('Параметры', {
            'fields': ('suits_name', 'url',), 'classes': ['wide']
        }),
        ('Изображения', {
            'fields': ('image_1', 'image_2', 'image_3', 'image_4'),
            'classes': ['wide']
        }),
        ('Описания', {
            'fields': ('description', 'positive_description', 'negative_description', 'keywords', 'astrological_signs',
                       'alternative_names'), 'classes': ['wide']
        }),
        ('SEO', {
            'fields': ('seo_description', 'seo_tags'), 'classes': ['wide']
        }),
    )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'card_suit')
    list_filter = ('card_suit',)
    search_fields = ('name', 'card_suit__suits_name')
    prepopulated_fields = {'url': ('url',)}
    fieldsets = (
        ('Параметры', {'fields': ('name', 'card_suit', 'image_1'), 'classes': ['wide']}),
        ('URL', {'fields': ('url',), 'classes': ['wide']}),
        ('Общее значение',
         {'fields': ('general_meaning', 'general_up', 'general_down', 'general_up_tags', 'general_down_tags'),
          'classes': ['wide']}),
        ('Значение для любви', {'fields': ('love_up', 'love_down', 'love_up_tags', 'love_down_tags'), 'classes': ['wide']}),
        ('Значение для работы', {'fields': ('career_up', 'career_down', 'career_up_tags', 'career_down_tags'), 'classes': ['wide']}),
        ('Значение для финансов',
         {'fields': ('finance_up', 'finance_down', 'finance_up_tags', 'finance_down_tags'), 'classes': ['wide']}),
        ('Прошлое, настоящее, будущее', {'fields': ('past_meaning', 'present_meaning', 'future_meaning'), 'classes': ['wide']}),
        ('Совет', {'fields': ('card_of_day', 'card_advice', 'yes_no'), 'classes': ['wide']}),
        ('SEO', {'fields': ('seo_description', 'seo_key_words'), 'classes': ['wide']}),

    )
