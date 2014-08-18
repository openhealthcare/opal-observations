"""
Models for the OPAL observations plugin
"""
from django.db import models

from opal.models import EpisodeSubrecord

class Observation(EpisodeSubrecord):
    _batch_template = True
    _sort           = 'date'

    bp_systolic  = models.FloatField(blank=True, null=True)
    bp_diastolic = models.FloatField(blank=True, null=True)
    pulse        = models.FloatField(blank=True, null=True)
    resp_rate    = models.FloatField(blank=True, null=True)
    sp02         = models.FloatField(blank=True, null=True)
    temperature  = models.FloatField(blank=True, null=True)
    height       = models.FloatField(blank=True, null=True)
    weight       = models.FloatField(blank=True, null=True)
    date         = models.DateField(blank=True, null=True)
    time         = models.IntegerField(blank=True, null=True)
