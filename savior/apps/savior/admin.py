from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin

from savior.apps.savior.models import Carousel



class CarouselAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'active')


admin.site.register(Carousel, CarouselAdmin)