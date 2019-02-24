# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'About'
        db.create_table(u'menu_about', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug_pl', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('slug_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('title_pl', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('short_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('short_text_pl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('short_text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('long_text', self.gf('ckeditor.fields.RichTextField')()),
            ('long_text_pl', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('long_text_en', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'menu', ['About'])

        # Adding model 'Ministry'
        db.create_table(u'menu_ministry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug_pl', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('slug_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('title_pl', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('short_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('short_text_pl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('short_text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('long_text', self.gf('ckeditor.fields.RichTextField')()),
            ('long_text_pl', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('long_text_en', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'menu', ['Ministry'])

        # Adding model 'Project'
        db.create_table(u'menu_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug_pl', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('slug_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('title_pl', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('short_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('short_text_pl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('short_text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('long_text', self.gf('ckeditor.fields.RichTextField')()),
            ('long_text_pl', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('long_text_en', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'menu', ['Project'])

        # Adding model 'Course'
        db.create_table(u'menu_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug_pl', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('slug_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('title_pl', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('short_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('short_text_pl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('short_text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('long_text', self.gf('ckeditor.fields.RichTextField')()),
            ('long_text_pl', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('long_text_en', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'menu', ['Course'])

        # Adding model 'Contact'
        db.create_table(u'menu_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_prefix', self.gf('django.db.models.fields.TextField')()),
            ('address_prefix_pl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address_prefix_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address', self.gf('geoposition.fields.GeopositionField')(max_length=42)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('bank', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('bank_pl', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('bank_en', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'menu', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'About'
        db.delete_table(u'menu_about')

        # Deleting model 'Ministry'
        db.delete_table(u'menu_ministry')

        # Deleting model 'Project'
        db.delete_table(u'menu_project')

        # Deleting model 'Course'
        db.delete_table(u'menu_course')

        # Deleting model 'Contact'
        db.delete_table(u'menu_contact')


    models = {
        u'menu.about': {
            'Meta': {'ordering': "('order',)", 'object_name': 'About'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_text': ('ckeditor.fields.RichTextField', [], {}),
            'long_text_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'long_text_pl': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'short_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_text_pl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'slug_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'menu.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('geoposition.fields.GeopositionField', [], {'max_length': '42'}),
            'address_prefix': ('django.db.models.fields.TextField', [], {}),
            'address_prefix_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'address_prefix_pl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bank': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'bank_en': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'bank_pl': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'menu.course': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Course'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'long_text': ('ckeditor.fields.RichTextField', [], {}),
            'long_text_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'long_text_pl': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'short_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_text_pl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'slug_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'menu.ministry': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Ministry'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'long_text': ('ckeditor.fields.RichTextField', [], {}),
            'long_text_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'long_text_pl': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'short_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_text_pl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'slug_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'menu.project': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'long_text': ('ckeditor.fields.RichTextField', [], {}),
            'long_text_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'long_text_pl': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'short_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_text_pl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'slug_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['menu']