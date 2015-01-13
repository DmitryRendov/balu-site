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
            name='AttributeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=1, max_length=15, choices=[(b'Text', b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5'), (b'Number', b'\xd0\xa7\xd0\xb8\xd1\x81\xd0\xbb\xd0\xbe'), (b'Image', b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0'), (b'Album', b'\xd0\x90\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc'), (b'Date', b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'), (b'Time', b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f')])),
                ('description', models.CharField(max_length=150)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 1, 12, 9, 8, 8, 292156), auto_now_add=True)),
                ('modified', models.DateTimeField(default=datetime.datetime(2015, 1, 12, 9, 8, 8, 292188), auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField(null=True, verbose_name=b'\xd0\x97\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 1, 12, 9, 8, 8, 291116), auto_now_add=True)),
                ('modified', models.DateTimeField(default=datetime.datetime(2015, 1, 12, 9, 8, 8, 291173), auto_now_add=True)),
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
                ('description', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x89\xd0\xb5\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('thumb', models.ImageField(upload_to=b'thumbs', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x82\xd0\xb8\xd0\xbf', blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 1, 12, 9, 8, 8, 293028), auto_now_add=True)),
                ('modified', models.DateTimeField(default=datetime.datetime(2015, 1, 12, 9, 8, 8, 293056), auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('attributes', models.ManyToManyField(to='inventory.AttributeType')),
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
                ('created', models.DateTimeField(default=datetime.datetime(2015, 1, 12, 9, 8, 8, 806775))),
                ('modified', models.DateTimeField(default=datetime.datetime(2015, 1, 12, 9, 8, 8, 806819), auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, to='album.Album', null=True)),
                ('inventory', models.ForeignKey(to='inventory.Inventory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attributetype',
            name='value',
            field=models.ForeignKey(blank=True, to='inventory.AttributeValue', null=True),
            preserve_default=True,
        ),
    ]
