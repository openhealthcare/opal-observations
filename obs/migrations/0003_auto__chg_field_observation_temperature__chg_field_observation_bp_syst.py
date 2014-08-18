# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Observation.temperature'
        db.alter_column(u'obs_observation', 'temperature', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Observation.bp_systolic'
        db.alter_column(u'obs_observation', 'bp_systolic', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Observation.bp_diastolic'
        db.alter_column(u'obs_observation', 'bp_diastolic', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Observation.weight'
        db.alter_column(u'obs_observation', 'weight', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Observation.height'
        db.alter_column(u'obs_observation', 'height', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Observation.pulse'
        db.alter_column(u'obs_observation', 'pulse', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Observation.sp02'
        db.alter_column(u'obs_observation', 'sp02', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Observation.resp_rate'
        db.alter_column(u'obs_observation', 'resp_rate', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'Observation.temperature'
        db.alter_column(u'obs_observation', 'temperature', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Observation.bp_systolic'
        db.alter_column(u'obs_observation', 'bp_systolic', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Observation.bp_diastolic'
        db.alter_column(u'obs_observation', 'bp_diastolic', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Observation.weight'
        db.alter_column(u'obs_observation', 'weight', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Observation.height'
        db.alter_column(u'obs_observation', 'height', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Observation.pulse'
        db.alter_column(u'obs_observation', 'pulse', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Observation.sp02'
        db.alter_column(u'obs_observation', 'sp02', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Observation.resp_rate'
        db.alter_column(u'obs_observation', 'resp_rate', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'obs.observation': {
            'Meta': {'object_name': 'Observation'},
            'bp_diastolic': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bp_systolic': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']", 'null': 'True'}),
            'height': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pulse': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'resp_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sp02': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
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