from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import ColorCharacter, MonthDayCharacter, WeekDayCharacter


class CharacterAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ColorCharacter
        fields = '__all__'


class BaseCharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'moderation')
    list_filter = ('moderation',)
    search_fields = ('name',)
    form = CharacterAdminForm

    fieldsets = (
        ('Основные параметры', {
            'fields': ('name', 'color_code', 'text'), 'classes': ['wide']
        }),
        ('SEO', {
            'fields': ('seo_description', 'seo_keywords'), 'classes': ['wide']
        }),
        ('Дополнительные параметры', {
            'fields': ('url', 'moderation'), 'classes': ['wide']
        }),
    )


@admin.register(ColorCharacter)
class ColorCharacterAdmin(BaseCharacterAdmin):
    pass


@admin.register(WeekDayCharacter)
class WeekDayCharacterAdmin(BaseCharacterAdmin):
    pass


@admin.register(MonthDayCharacter)
class MonthDayCharacterAdmin(BaseCharacterAdmin):
    pass
