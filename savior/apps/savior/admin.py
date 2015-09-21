from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin
from modeltranslation.admin import TranslationAdmin

from savior.apps.savior.models import Carousel, PrayerRequest, Footer


class PrayerRequestAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields]
            
        return self.readonly_fields


class CarouselAdmin(SortableAdminMixin, TranslationAdmin):
    list_display = ('title', 'active')


admin.site.register(Footer, TranslationAdmin)
admin.site.register(PrayerRequest, PrayerRequestAdmin)
admin.site.register(Carousel, CarouselAdmin)