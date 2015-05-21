# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('market', models.CharField(default=b'None', max_length=50)),
                ('code', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'NO NAME!', max_length=50)),
            ],
        ),
    ]
