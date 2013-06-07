# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Part.unit'
        db.add_column(u'inventory_part', 'unit',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Part.unit'
        db.delete_column(u'inventory_part', 'unit')


    models = {
        u'inventory.part': {
            'Meta': {'object_name': 'Part'},
            'from_value': ('django.db.models.fields.FloatField', [], {}),
            'general_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'package': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Place']"}),
            'remaining': ('django.db.models.fields.IntegerField', [], {}),
            'specific_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to_value': ('django.db.models.fields.FloatField', [], {}),
            'unit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'inventory.place': {
            'Meta': {'object_name': 'Place'},
            'column': ('django.db.models.fields.IntegerField', [], {}),
            'depth': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['inventory']