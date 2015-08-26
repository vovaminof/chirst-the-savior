from django.db import models
from geoposition.fields import GeopositionField
from recurrence.fields import RecurrenceField
from taggit.managers import TaggableManager


class Event(models.Model):
    tags = TaggableManager()

    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.FileField(upload_to='events')
    start = models.TimeField()
    end = models.TimeField()
    recurrences = RecurrenceField()
    place = GeopositionField()
    join_link = models.CharField(max_length=128)
    join_text = models.CharField(max_length=32)