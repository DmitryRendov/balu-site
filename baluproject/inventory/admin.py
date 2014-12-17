# coding=utf-8
from django.contrib import admin
from inventory.models import Inventory, InventoryItem
from inventory.models import Album, Photo
from mptt.admin import MPTTModelAdmin

class InventoryAdmin(MPTTModelAdmin):
    fieldsets = [
        (None,             {'fields': ['name', 'parent']}),
        ('Описание',       {'fields': ['description']}),
        ('Это контейнер?', {'fields': ['is_container']}),
    ]
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryItem)


class AlbumInline(admin.StackedInline):
    model = Photo
    extra = 2

class AlbumAdmin(admin.ModelAdmin):
    """fieldsets = [
        (None,             {'fields': ['summary', 'image']}),
        ('Это обложка?', {'fields': ['is_cover_photo']}),
        ('Date info', {'fields': ['date_created', 'date_modified'], 'classes': ['collapse']}),
    ]"""
    inlines = [AlbumInline]

admin.site.register(Album, AlbumAdmin)

