from modeltranslation.translator import translator, TranslationOptions
from savior.apps.menu.models import About, Ministry, Project, Course


class MenuTranslationOptions(TranslationOptions):
    fields = ('slug', 'title', 'short_text', 'long_text')

translator.register(Ministry, MenuTranslationOptions)
translator.register(About, MenuTranslationOptions)
translator.register(Project, MenuTranslationOptions)
translator.register(Course, MenuTranslationOptions)