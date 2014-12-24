# coding=utf-8
from django.contrib import admin
from album.models import Album, Photo

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