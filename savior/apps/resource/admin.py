from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin
from modeltranslation.admin import TranslationAdmin

from savior.apps.resource.models import Category, Resource, File


class CategoryAdmin(SortableAdminMixin, TranslationAdmin):
    pass


class ResourceAdmin(SortableAdminMixin, TranslationAdmin):
    list_display = ('title', 'category', 'active')


admin.site.register(File)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Resource, ResourceAdmin)
