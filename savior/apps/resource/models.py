from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class Resource(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True)
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
