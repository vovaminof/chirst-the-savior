from django.conf import settings
from django.db import models


class CarouselManager(models.Manager):

    def get_active(self):
        return self.filter(active=True).order_by('order')


class Carousel(models.Model):
    LINK_MODES = (
        ('_blank', 'Opens in a new tab.'),
        ('_self', 'Opens in the same frame.')
    )

    objects = CarouselManager()

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    image = models.FileField(upload_to='carousel')
    title = models.CharField(max_length=128)
    long_text = models.CharField(max_length=256)
    link = models.CharField(max_length=256, default=None, null=True, blank=True)
    link_text = models.CharField(max_length=256, default=settings.DEFAULT_CAROUSEL_LINK_TEXT, 
                                 null=True, blank=True)
    link_mode = models.CharField(max_length=6, choices=LINK_MODES, default=None, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    class Meta(object):
        ordering = ('order',)