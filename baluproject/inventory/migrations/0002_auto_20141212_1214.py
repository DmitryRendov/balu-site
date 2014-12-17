# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 12, 12, 14, 3, 541319)),
            preserve_default=True,
        ),
    ]
