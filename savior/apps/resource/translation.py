from modeltranslation.translator import translator, TranslationOptions
from savior.apps.resource.models import Resource, Category, Book


class ResourceTranslationOptions(TranslationOptions):
    fields = ('title',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'short_text', 'description')


translator.register(Resource, ResourceTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Book, BookTranslationOptions)

