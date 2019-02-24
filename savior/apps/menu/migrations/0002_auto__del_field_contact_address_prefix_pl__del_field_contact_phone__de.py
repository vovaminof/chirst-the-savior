# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contact.address_prefix_pl'
        db.delete_column(u'menu_contact', 'address_prefix_pl')

        # Deleting field 'Contact.phone'
        db.delete_column(u'menu_contact', 'phone')

        # Deleting field 'Contact.address_prefix_en'
        db.delete_column(u'menu_contact', 'address_prefix_en')

        # Deleting field 'Contact.address_prefix'
        db.delete_column(u'menu_contact', 'address_prefix')

        # Deleting field 'Contact.bank'
        db.delete_column(u'menu_contact', 'bank')

        # Deleting field 'Contact.bank_pl'
        db.delete_column(u'menu_contact', 'bank_pl')

        # Deleting field 'Contact.bank_en'
        db.delete_column(u'menu_contact', 'bank_en')

        # Deleting field 'Contact.email'
        db.delete_column(u'menu_contact', 'email')

        # Adding field 'Contact.address_pl'
        db.add_column(u'menu_contact', 'address_pl',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.address_en'
        db.add_column(u'menu_contact', 'address_en',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.text'
        db.add_column(u'menu_contact', 'text',
                      self.gf('ckeditor.fields.RichTextField')(default='TBD'),
                      keep_default=False)

        # Adding field 'Contact.text_pl'
        db.add_column(u'menu_contact', 'text_pl',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.text_en'
        db.add_column(u'menu_contact', 'text_en',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Contact.address'
        db.alter_column(u'menu_contact', 'address', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Adding field 'Contact.address_prefix_pl'
        db.add_column(u'menu_contact', 'address_prefix_pl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Contact.phone'
        raise RuntimeError("Cannot reverse this migration. 'Contact.phone' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contact.phone'
        db.add_column(u'menu_contact', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=32),
                      keep_default=False)

        # Adding field 'Contact.address_prefix_en'
        db.add_column(u'menu_contact', 'address_prefix_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Contact.address_prefix'
        raise RuntimeError("Cannot reverse this migration. 'Contact.address_prefix' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contact.address_prefix'
        db.add_column(u'menu_contact', 'address_prefix',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Contact.bank'
        raise RuntimeError("Cannot reverse this migration. 'Contact.bank' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contact.bank'
        db.add_column(u'menu_contact', 'bank',
                      self.gf('django.db.models.fields.CharField')(max_length=128),
                      keep_default=False)

        # Adding field 'Contact.bank_pl'
        db.add_column(u'menu_contact', 'bank_pl',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.bank_en'
        db.add_column(u'menu_contact', 'bank_en',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Contact.email'
        raise RuntimeError("Cannot reverse this migration. 'Contact.email' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contact.email'
        db.add_column(u'menu_contact', 'email',
                      self.gf('django.db.models.fields.CharField')(max_length=32),
                      keep_default=False)

        # Deleting field 'Contact.address_pl'
        db.delete_column(u'menu_contact', 'address_pl')

        # Deleting field 'Contact.address_en'
        db.delete_column(u'menu_contact', 'address_en')

        # Deleting field 'Contact.text'
        db.delete_column(u'menu_contact', 'text')

        # Deleting field 'Contact.text_pl'
        db.delete_column(u'menu_contact', 'text_pl')

        # Deleting field 'Contact.text_en'
        db.delete_column(u'menu_contact', 'text_en')


        # Changing field 'Contact.address'
        db.alter_column(u'menu_contact', 'address', self.gf('geoposition.fields.GeopositionField')(max_length=42))

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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'address_en': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'address_pl': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {}),
            'text_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'text_pl': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'})
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