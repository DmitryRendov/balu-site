# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81')),
                ('description', models.TextField(null=True, blank=True)),
                ('is_container', models.BooleanField(default=False)),
                ('thumb', models.ImageField(upload_to=b'thumbs', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(related_name='child', verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to='inventory.Inventory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime(2014, 12, 24, 6, 50, 35, 777124))),
                ('album', models.ForeignKey(to='album.Album')),
                ('inventory', models.ForeignKey(to='inventory.Inventory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
