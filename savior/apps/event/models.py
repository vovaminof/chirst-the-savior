from events.models import Event as SimpleEvent
from geoposition.fields import GeopositionField
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

from django.db import models
from django.contrib.contenttypes import generic



class Event(models.Model):
    tags = TaggableManager()

    title = models.CharField(max_length=64)
    description = RichTextField()
    image = models.FileField(upload_to='events')
    recurrences = generic.GenericRelation(SimpleEvent)
    place = GeopositionField()
    join_link = models.CharField(max_length=128, blank=True)
    join_text = models.CharField(max_length=32, blank=True)

    def __unicode__(self):
        return self.title 