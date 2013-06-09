# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Place.depth'
        db.delete_column(u'inventory_place', 'depth')

        # Deleting field 'Place.column'
        db.delete_column(u'inventory_place', 'column')

        # Deleting field 'Place.row'
        db.delete_column(u'inventory_place', 'row')

        # Deleting field 'Place.module'
        db.delete_column(u'inventory_place', 'module')

        # Deleting field 'Place.room'
        db.delete_column(u'inventory_place', 'room')

        # Adding field 'Place.parent'
        db.add_column(u'inventory_place', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['inventory.Place']),
                      keep_default=False)

        # Adding field 'Place.type'
        db.add_column(u'inventory_place', 'type',
                      self.gf('django.db.models.fields.CharField')(default='Space', max_length=255),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Place.depth'
        raise RuntimeError("Cannot reverse this migration. 'Place.depth' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Place.column'
        raise RuntimeError("Cannot reverse this migration. 'Place.column' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Place.row'
        raise RuntimeError("Cannot reverse this migration. 'Place.row' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Place.module'
        raise RuntimeError("Cannot reverse this migration. 'Place.module' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Place.room'
        raise RuntimeError("Cannot reverse this migration. 'Place.room' and its values cannot be restored.")
        # Deleting field 'Place.parent'
        db.delete_column(u'inventory_place', 'parent_id')

        # Deleting field 'Place.type'
        db.delete_column(u'inventory_place', 'type')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['inventory.Place']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['inventory']