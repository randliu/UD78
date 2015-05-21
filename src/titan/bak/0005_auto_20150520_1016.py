# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titan', '0004_auto_20150520_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risetrack',
            name='beginDay',
            field=models.IntegerField(default=0),
        ),
    ]
