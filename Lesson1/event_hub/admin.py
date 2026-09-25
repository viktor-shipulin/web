from django.contrib import admin
from django.utils.html import format_html
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'starts_at', 'is_published', 'poster_preview')

    def poster_preview(self, obj):
        if obj.poster:
            return format_html('<img src="{}" style="height: 50px;">', obj.poster.url)
        return '—'
    poster_preview.short_description = 'Постер'

admin.site.register(Event, EventAdmin)