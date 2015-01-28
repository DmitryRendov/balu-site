# coding=utf-8
from datetime import datetime
from django.db import models
from django.utils.encoding import force_unicode
from album.models import Album

class InventoryItem(models.Model):
    inventory = models.ForeignKey('Inventory')
    album = models.ForeignKey(Album, blank=True, null=True)
    amount = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.now())
    modified = models.DateTimeField(default=datetime.now(), auto_now_add=True)

    def __unicode__(self):
        return force_unicode("%s %s" % (self.inventory, self.amount))

    class Meta:
        verbose_name = u'Объект инвентаря'
        verbose_name_plural = u'Объекты инвентаря'
