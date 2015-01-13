# coding=utf-8
from datetime import datetime
from django.db import models
from django.utils.encoding import force_unicode

ATTRIBUTE_CHOICES = (
    ('Text', 'Текстовое поле'),
    ('Number', 'Число'),
    ('Image', 'Картинка'),
    ('Album', 'Альбом'),
    ('Date', 'Дата'),
    ('Time', 'Время'),
)

class AttributeValue(models.Model):
    value = models.TextField("Значение", blank=True, null=True)
    created = models.DateTimeField(default=datetime.now(), auto_now_add=True)
    modified = models.DateTimeField(default=datetime.now(), auto_now_add=True)
    def __unicode__(self):
        return force_unicode("%s" % (self.value))

class AttributeType(models.Model):
    type = models.CharField(max_length=15, choices=ATTRIBUTE_CHOICES, default=1)
    description = models.CharField(max_length=150, blank=True)
    value = models.ForeignKey(AttributeValue, blank=True, null=True)
    created = models.DateTimeField(default=datetime.now(), auto_now_add=True)
    modified = models.DateTimeField(default=datetime.now(), auto_now_add=True)
    def __unicode__(self):
        return force_unicode("%s" % (self.type))

