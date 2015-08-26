from django.db import models


class Bulletin(models.Model):
    src = models.FileField(upload_to='bulletins')
    publish_date = models.DateField()

    def __str__(self):
        return '{:%d, %b %Y}'.format(self.publish_date)
