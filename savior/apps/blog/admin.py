from modeltranslation.admin import TranslationAdmin

from django.contrib import admin

from savior.apps.blog.models import Post, Author


class PostAdmin(TranslationAdmin):
    list_display = ('title', 'published', 'author', 'ctime')

admin.site.register(Post, PostAdmin)
admin.site.register(Author, TranslationAdmin)
