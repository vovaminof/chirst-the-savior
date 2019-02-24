# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Footer.contact'
        db.delete_column(u'savior_footer', 'contact_id')

        # Adding field 'Footer.address'
        db.add_column(u'savior_footer', 'address',
                      self.gf('django.db.models.fields.CharField')(default='D\xc5\x82uga 3, Krak\xc3\xb3w, Polska', max_length=128),
                      keep_default=False)

        # Adding field 'Footer.phone'
        db.add_column(u'savior_footer', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='+48 665 670 712', max_length=32),
                      keep_default=False)

        # Adding field 'Footer.email'
        db.add_column(u'savior_footer', 'email',
                      self.gf('django.db.models.fields.CharField')(default='kosciolzbawiciela@gmail.com', max_length=32),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Footer.contact'
        raise RuntimeError("Cannot reverse this migration. 'Footer.contact' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Footer.contact'
        db.add_column(u'savior_footer', 'contact',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Contact']),
                      keep_default=False)

        # Deleting field 'Footer.address'
        db.delete_column(u'savior_footer', 'address')

        # Deleting field 'Footer.phone'
        db.delete_column(u'savior_footer', 'phone')

        # Deleting field 'Footer.email'
        db.delete_column(u'savior_footer', 'email')


    models = {
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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'facebook_link': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32'})
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