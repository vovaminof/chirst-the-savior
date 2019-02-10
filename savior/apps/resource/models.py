from django.db import models

from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=64)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class Resource(models.Model):
    category = models.ForeignKey(Category, null=False, blank=False)
    title = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class File(models.Model):
    resource = models.ForeignKey(Resource)
    file_format = models.CharField(max_length=16, null=True, blank=True)
    link = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        result = self.resource.title
        if self.file_format:
            result += " [%s]" % (self.file_format,)

        return result


class Book(models.Model):
    category = models.ForeignKey(Category, null=False, blank=False)
    title = models.CharField(max_length=64)
    short_text = models.CharField(max_length=256, null=True, blank=True)
    description = RichTextField()
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('order',)

