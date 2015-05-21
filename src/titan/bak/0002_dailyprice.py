# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPrice',
            fields=[
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('day', models.IntegerField(default=0)),
                ('open', models.FloatField(default=0)),
                ('close', models.FloatField(default=0)),
                ('high', models.FloatField(default=0)),
                ('low', models.FloatField(default=0)),
                ('onClose', models.CharField(default=b'RISE', max_length=50)),
                ('stock', models.ForeignKey(to='titan.Stock')),
            ],
        ),
    ]
