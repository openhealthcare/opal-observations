# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obs', '0002_observation_episode'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='observation',
            name='created_by',
            field=models.ForeignKey(related_name='created_obs_observation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='observation',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='observation',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_obs_observation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE),
        ),
    ]
