# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Part.specific_type'
        db.alter_column(u'inventory_part', 'specific_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Part.package'
        db.alter_column(u'inventory_part', 'package', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Part.note'
        db.alter_column(u'inventory_part', 'note', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Part.to_value'
        db.alter_column(u'inventory_part', 'to_value', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Part.general_type'
        db.alter_column(u'inventory_part', 'general_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Part.from_value'
        db.alter_column(u'inventory_part', 'from_value', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Part.unit'
        db.alter_column(u'inventory_part', 'unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Part.specific_type'
        db.alter_column(u'inventory_part', 'specific_type', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Part.package'
        db.alter_column(u'inventory_part', 'package', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Part.note'
        db.alter_column(u'inventory_part', 'note', self.gf('django.db.models.fields.TextField')(default=''))

        # User chose to not deal with backwards NULL issues for 'Part.to_value'
        raise RuntimeError("Cannot reverse this migration. 'Part.to_value' and its values cannot be restored.")

        # Changing field 'Part.general_type'
        db.alter_column(u'inventory_part', 'general_type', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # User chose to not deal with backwards NULL issues for 'Part.from_value'
        raise RuntimeError("Cannot reverse this migration. 'Part.from_value' and its values cannot be restored.")

        # Changing field 'Part.unit'
        db.alter_column(u'inventory_part', 'unit', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'inventory.part': {
            'Meta': {'object_name': 'Part'},
            'from_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'general_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'package': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Place']"}),
            'remaining': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'specific_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'to_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
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