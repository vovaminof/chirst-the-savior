from modeltranslation.translator import translator, TranslationOptions
from savior.apps.menu.models import About, Ministry, Project, Course, Contact


class MenuTranslationOptions(TranslationOptions):
    fields = ('slug', 'title', 'short_text', 'long_text')


class ContactTranslation(TranslationOptions):
	fields = ('address_prefix', 'bank')


translator.register(Ministry, MenuTranslationOptions)
translator.register(About, MenuTranslationOptions)
translator.register(Project, MenuTranslationOptions)
translator.register(Course, MenuTranslationOptions)
translator.register(Contact, ContactTranslation)