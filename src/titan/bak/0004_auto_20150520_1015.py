# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titan', '0003_droptrack_ladder_peakpoint_risetrack_troughpoint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='risetrack',
            old_name='endDay',
            new_name='beginValue',
        ),
        migrations.RenameField(
            model_name='risetrack',
            old_name='value',
            new_name='lastDay',
        ),
        migrations.AddField(
            model_name='risetrack',
            name='lastValue',
            field=models.IntegerField(default=0),
        ),
    ]
