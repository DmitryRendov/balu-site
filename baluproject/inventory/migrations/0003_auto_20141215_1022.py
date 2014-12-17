# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20141212_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
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
        migrations.RemoveField(
            model_name='image',
            name='album',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 10, 22, 40, 165350)),
            preserve_default=True,
        ),
    ]
