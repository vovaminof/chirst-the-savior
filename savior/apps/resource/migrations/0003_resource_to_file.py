# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        formats = (" PDF", " epub")
        grouped = {}
        for resource in orm.Resource.objects.all():
            resource_format = None
            for file_format in formats:
                if resource.title.lower().endswith(file_format.lower()):
                    title = resource.title_pl[:-len(file_format)]
                    resource_format = file_format.strip()
                    break
            else:
                title = resource.title_pl
            grouped.setdefault(title, []).append({
                "category": resource.category,
                "file_format": resource_format,
                "link": resource.link,
                "active": resource.active
            })
        orm.Resource.objects.all().delete()
        for title, files in grouped.items():
            resource = orm.Resource(category=files[0]["category"], title_pl=title, link="will be removed")
            resource.save()

            for _file in files:
                resource_file = orm.File(resource=resource, file_format=_file["file_format"],
                                         link=_file["link"], active=_file["active"])
                resource_file.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'resource.category': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'resource.file': {
            'Meta': {'object_name': 'File'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'file_format': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null':
                                                                      'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resource.Resource']"})
        },
        u'resource.resource': {
            'Meta': {'object_name': 'Resource'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resource.Category']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['resource']
    symmetrical = True
