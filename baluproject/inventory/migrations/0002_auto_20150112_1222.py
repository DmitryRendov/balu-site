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
            model_name='attributetype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 12, 22, 35, 773777), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attributetype',
            name='description',
            field=models.CharField(max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attributetype',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 12, 22, 35, 773807), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 12, 22, 35, 772746), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 12, 22, 35, 772798), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='attributes',
            field=models.ManyToManyField(to='inventory.AttributeType', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 12, 22, 35, 775056), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 12, 22, 35, 775098), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 12, 22, 36, 162622)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 12, 22, 36, 162678), auto_now_add=True),
            preserve_default=True,
        ),
    ]
