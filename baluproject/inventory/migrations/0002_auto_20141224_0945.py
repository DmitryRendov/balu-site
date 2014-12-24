# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='is_container',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 24, 9, 45, 38, 866775)),
            preserve_default=True,
        ),
    ]
