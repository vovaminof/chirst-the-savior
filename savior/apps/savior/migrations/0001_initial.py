# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carousel'
        db.create_table(u'savior_carousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('title_pl', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('long_text', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('long_text_pl', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('long_text_en', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(default=None, max_length=256, null=True, blank=True)),
            ('link_text', self.gf('django.db.models.fields.CharField')(default='Learn more', max_length=256, null=True, blank=True)),
            ('link_text_pl', self.gf('django.db.models.fields.CharField')(default='Learn more', max_length=256, null=True, blank=True)),
            ('link_text_en', self.gf('django.db.models.fields.CharField')(default='Learn more', max_length=256, null=True, blank=True)),
            ('link_mode', self.gf('django.db.models.fields.CharField')(default=None, max_length=6, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'savior', ['Carousel'])

        # Adding model 'Footer'
        db.create_table(u'savior_footer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Contact'])),
            ('about_text', self.gf('django.db.models.fields.TextField')()),
            ('about_text_pl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('about_text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('facebook_link', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'savior', ['Footer'])

        # Adding model 'PrayerRequest'
        db.create_table(u'savior_prayerrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'savior', ['PrayerRequest'])


    def backwards(self, orm):
        # Deleting model 'Carousel'
        db.delete_table(u'savior_carousel')

        # Deleting model 'Footer'
        db.delete_table(u'savior_footer')

        # Deleting model 'PrayerRequest'
        db.delete_table(u'savior_prayerrequest')


    models = {
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
        u'savior.carousel': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Carousel'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'link_mode': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'default': "'Learn more'", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'link_text_en': ('django.db.models.fields.CharField', [], {'default': "'Learn more'", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'link_text_pl': ('django.db.models.fields.CharField', [], {'default': "'Learn more'", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'long_text': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'long_text_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'long_text_pl': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'savior.footer': {
            'Meta': {'object_name': 'Footer'},
            'about_text': ('django.db.models.fields.TextField', [], {}),
            'about_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_text_pl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.Contact']"}),
            'facebook_link': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'savior.prayerrequest': {
            'Meta': {'object_name': 'PrayerRequest'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['savior']