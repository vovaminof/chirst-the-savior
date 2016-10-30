from modeltranslation.translator import translator, TranslationOptions
from savior.apps.resource.models import Resource, Category


class ResourceTranslationOptions(TranslationOptions):
    fields = ('title',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Resource, ResourceTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
