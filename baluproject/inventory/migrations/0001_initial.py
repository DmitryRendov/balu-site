# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
        ('attributes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81')),
                ('description', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x89\xd0\xb5\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('thumb', models.ImageField(upload_to=b'thumbs', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb8\xd0\xbf', blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 1, 28, 9, 11, 13, 378278), auto_now_add=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('attributes', models.ManyToManyField(to='attributes.Attribute', blank=True)),
                ('parent', models.ForeignKey(related_name='child', verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to='inventory.Inventory', null=True)),
            ],
            options={
                'verbose_name': '\u041a\u043b\u0430\u0441\u0441 \u0438\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u044f',
                'verbose_name_plural': '\u041a\u043b\u0430\u0441\u0441\u044b \u0438\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 1, 28, 9, 11, 13, 407282))),
                ('modified', models.DateTimeField(default=datetime.datetime(2015, 1, 28, 9, 11, 13, 407313), auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, to='album.Album', null=True)),
                ('inventory', models.ForeignKey(to='inventory.Inventory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
