# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titan', '0002_dailyprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropTrack',
            fields=[
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('beginDay', models.IntegerField(default=0, unique=True)),
                ('endDay', models.IntegerField(default=0)),
                ('value', models.IntegerField(default=0)),
                ('status', models.CharField(default=b'RUN', max_length=50)),
                ('stock', models.ForeignKey(to='titan.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Ladder',
            fields=[
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('day', models.IntegerField(default=0, unique=True)),
                ('ladder', models.IntegerField(default=0)),
                ('stock', models.ForeignKey(to='titan.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='PeakPoint',
            fields=[
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('day', models.IntegerField(default=0, unique=True)),
                ('stock', models.ForeignKey(to='titan.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='RiseTrack',
            fields=[
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('beginDay', models.IntegerField(default=0, unique=True)),
                ('endDay', models.IntegerField(default=0)),
                ('value', models.IntegerField(default=0)),
                ('status', models.CharField(default=b'RUN', max_length=50)),
                ('stock', models.ForeignKey(to='titan.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='TroughPoint',
            fields=[
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('day', models.IntegerField(default=0, unique=True)),
                ('stock', models.ForeignKey(to='titan.Stock')),
            ],
        ),
    ]
