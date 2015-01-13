# coding=utf-8
import mptt
from datetime import datetime
from django.db import models
from django.utils.encoding import force_unicode
from attribute import AttributeType

class Inventory(models.Model):
    name = models.CharField("Класс", max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="Родитель", related_name='child')
    description = models.TextField("Общее описание", blank=True, null=True)
    thumb = models.ImageField("Логотип", upload_to='thumbs',blank=True)
    created = models.DateTimeField(default=datetime.now(), auto_now_add=True)
    modified = models.DateTimeField(default=datetime.now(), auto_now_add=True)
    attributes = models.ManyToManyField(AttributeType, blank=True)

    def __unicode__(self):
        return force_unicode("%s %s" % (self.name, self.description))

mptt.register(Inventory,)
