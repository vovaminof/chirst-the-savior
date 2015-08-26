from ckeditor.fields import RichTextField

from django.conf import settings
from django.db import models


class AboutManager(models.Manager):

    def get_active(self):
        return self.filter(active=True).order_by('order')


class AbstractMenu(models.Model):

    objects = AboutManager()

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    slug = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    short_text = models.TextField(blank=True)
    long_text = RichTextField()

    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    class Meta(object):
        abstract = True
        ordering = ('order',)


class About(AbstractMenu):
    pass


class Ministry(AbstractMenu):
    image = models.FileField(upload_to='ministries')

    class Meta(AbstractMenu.Meta):
        verbose_name_plural = "Ministries"


class Project(AbstractMenu):
    image = models.FileField(upload_to='projects')


class Course(AbstractMenu):
    image = models.FileField(upload_to='courses')

     