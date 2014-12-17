# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('summary', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('summary', models.TextField(null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=b'inventory/images')),
                ('is_cover_photo', models.BooleanField(default=False)),
                ('album', models.ForeignKey(to='inventory.Album')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81')),
                ('description', models.TextField()),
                ('is_container', models.BooleanField(default=False)),
                ('thumb', models.ImageField(upload_to=b'inventory/thumbs')),
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
                ('created', models.DateTimeField(default=datetime.datetime(2014, 12, 12, 11, 38, 39, 387403))),
                ('album', models.ForeignKey(to='inventory.Album')),
                ('inventory', models.ForeignKey(to='inventory.Inventory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
