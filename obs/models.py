"""
Models for the OPAL observations plugin
"""
from django.db import models

from opal.models import EpisodeSubrecord

class Observation(EpisodeSubrecord):
    _batch_template = True
    _sort           = 'date'

    bp_systolic  = models.IntegerField(blank=True, null=True)
    bp_diastolic = models.IntegerField(blank=True, null=True)
    pulse        = models.IntegerField(blank=True, null=True)
    resp_rate    = models.IntegerField(blank=True, null=True)
    sp02         = models.IntegerField(blank=True, null=True)
    temperature  = models.IntegerField(blank=True, null=True)
    height       = models.IntegerField(blank=True, null=True)
    weight       = models.IntegerField(blank=True, null=True)
    date         = models.DateField(blank=True, null=True)
