# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import opal.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('bp_systolic', models.FloatField(null=True, blank=True)),
                ('bp_diastolic', models.FloatField(null=True, blank=True)),
                ('pulse', models.FloatField(null=True, blank=True)),
                ('resp_rate', models.FloatField(null=True, blank=True)),
                ('sp02', models.FloatField(null=True, blank=True)),
                ('temperature', models.FloatField(null=True, blank=True)),
                ('height', models.FloatField(null=True, blank=True)),
                ('weight', models.FloatField(null=True, blank=True)),
                ('datetime', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
    ]
