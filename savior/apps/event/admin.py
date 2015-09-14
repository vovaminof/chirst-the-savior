from events.admin import EventInline
from modeltranslation.admin import TranslationAdmin

from django.contrib import admin

from savior.apps.event.models import Event


class EventAdmin(TranslationAdmin):
    
    inlines = (EventInline,)


admin.site.register(Event, EventAdmin)