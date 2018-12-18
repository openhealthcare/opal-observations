# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0001_initial'),
        ('obs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='episode',
            field=models.ForeignKey(to='opal.Episode', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
