from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import ColorCharacter


class ColorCharacterAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ColorCharacter
        fields = '__all__'


@admin.register(ColorCharacter)
class ColorCharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'moderation')
    list_filter = ('moderation',)
    search_fields = ('name',)
    form = ColorCharacterAdminForm

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
