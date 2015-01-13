# coding=utf-8
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from inventory.models import Inventory
from inventory_item import InventoryItem
from attribute import AttributeType, AttributeValue

class InventoryAdmin(DjangoMpttAdmin):
    list_display = ('name', 'parent', 'description', 'thumb', 'created', 'modified')
    fieldsets = [
        (None,             {'fields': ['name', 'parent']}),
        ('Описание',       {'fields': ['description']}),
        ('Атрибуты',       {'fields': ['attributes']}),
        ('Картинка-логотип класса', {'fields': ['thumb']}),
    ]
    list_filter = ('created', 'modified',)

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'album', 'amount', 'created', 'modified')
    fieldsets = [
        (None,               {'fields': ['inventory']}),
        ('Описание',         {'fields': ['amount']}),
        ('Альбом',           {'fields': ['album']}),
    ]
    list_filter = ('created', 'modified',)


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(AttributeType)
admin.site.register(AttributeValue)


