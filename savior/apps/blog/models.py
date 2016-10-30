from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from datetime import datetime


class Author(models.Model):

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    about = models.TextField()
    image = models.FileField(upload_to='blog/author')

    def __unicode__(self):
        return u'{0.first_name} {0.last_name}'.format(self)


class Post(models.Model):
    tags = TaggableManager()

    title = models.CharField(max_length=64)
    text = RichTextField()
    ctime = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(Author)
    published = models.BooleanField(default=True)
    image = models.FileField(upload_to='blog')

    def __unicode__(self):
        return self.title
