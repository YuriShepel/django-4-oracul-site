from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')

    fieldsets = (
        ('Имя', {
            'fields': ('name',), 'classes': ['wide']
        }),
        ('Email', {
            'fields': ('email',), 'classes': ['wide']
        }),
        ('Текст сообщения', {
            'fields': ('message',), 'classes': ['wide']
        }),
        )
