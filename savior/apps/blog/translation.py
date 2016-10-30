from modeltranslation.translator import translator, TranslationOptions
from savior.apps.blog.models import Post, Author


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class AuthorTranslationOptions(TranslationOptions):
    fields = ('about',)


translator.register(Author, AuthorTranslationOptions)
translator.register(Post, PostTranslationOptions)
