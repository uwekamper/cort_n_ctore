# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'inventory_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('module', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('column', self.gf('django.db.models.fields.IntegerField')()),
            ('depth', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inventory', ['Place'])

        # Adding model 'Part'
        db.create_table(u'inventory_part', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('general_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('specific_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('from_value', self.gf('django.db.models.fields.FloatField')()),
            ('to_value', self.gf('django.db.models.fields.FloatField')()),
            ('package', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Place'])),
            ('note', self.gf('django.db.models.fields.TextField')()),
            ('remaining', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inventory', ['Part'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'inventory_place')

        # Deleting model 'Part'
        db.delete_table(u'inventory_part')


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
            'to_value': ('django.db.models.fields.FloatField', [], {})
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