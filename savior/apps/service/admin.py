from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from savior.apps.service.models import Bulletin


admin.site.register(Bulletin, TranslationAdmin)