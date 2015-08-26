from modeltranslation.translator import translator, TranslationOptions
from savior.apps.service.models import Bulletin


class BulettinTranslationOptions(TranslationOptions):
    fields = ('src',)

translator.register(Bulletin, BulettinTranslationOptions)