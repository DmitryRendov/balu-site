# coding=utf-8
from django.contrib import admin
from inventory.models import Inventory, InventoryItem
from mptt.admin import MPTTModelAdmin

class InventoryAdmin(MPTTModelAdmin):
    fieldsets = [
        (None,             {'fields': ['name', 'parent']}),
        ('Описание',       {'fields': ['description']}),
        ('Картинка класса', {'fields': ['thumb']}),
    ]
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryItem)

