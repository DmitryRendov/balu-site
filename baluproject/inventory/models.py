# coding=utf-8
import mptt
from datetime import datetime
from django.db import models
from django.utils.encoding import force_unicode
from album.models import Album

class Inventory(models.Model):
    name = models.CharField("Класс", max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="Родитель", related_name='child')
    description = models.TextField(blank=True, null=True)
    thumb = models.ImageField(upload_to='thumbs',blank=True)

    def __unicode__(self):
        return force_unicode("%s %s" % (self.name, self.description))

class InventoryItem(models.Model):
    inventory = models.ForeignKey('Inventory')
    album = models.ForeignKey(Album)
    amount = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.now())
    def __unicode__(self):
        return "%s %s" % (self.inventory, self.amount)

mptt.register(Inventory,)



