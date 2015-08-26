from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from savior.apps.event.models import Event


class EventAdmin(TranslationAdmin):
    pass


admin.site.register(Event, EventAdmin)