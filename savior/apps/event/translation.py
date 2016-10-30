from modeltranslation.translator import translator, TranslationOptions
from savior.apps.event.models import Event


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'join_text')

translator.register(Event, EventTranslationOptions)
