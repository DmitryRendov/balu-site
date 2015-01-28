# coding=utf-8
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from models import Inventory
from inventory_item import InventoryItem

class InventoryAdmin(DjangoMpttAdmin):
    list_display = ('name', 'parent', 'description', 'thumb', 'created', 'modified')
    fieldsets = [
        (None,             {'fields': ['name', 'parent']}),
        ('Описание',       {'fields': ['description']}),
        ('Атрибуты',       {'fields': ['global_attrs', 'local_attrs']}),
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
