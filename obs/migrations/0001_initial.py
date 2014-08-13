# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Observation'
        db.create_table(u'obs_observation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consistency_token', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Episode'], null=True)),
            ('bp_systolic', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('bp_diastolic', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pulse', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('resp_rate', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sp02', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('temperature', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'obs', ['Observation'])


    def backwards(self, orm):
        # Deleting model 'Observation'
        db.delete_table(u'obs_observation')


    models = {
        u'obs.observation': {
            'Meta': {'object_name': 'Observation'},
            'bp_diastolic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bp_systolic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']", 'null': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pulse': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resp_rate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sp02': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'temperature': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'opal.episode': {
            'Meta': {'object_name': 'Episode'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_of_admission': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'discharge_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Patient']"})
        },
        u'opal.patient': {
            'Meta': {'object_name': 'Patient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['obs']