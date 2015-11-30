from django.contrib import admin

# Register your models here.
from .models import Album, Image, Tag

class AlbumAdmin(admin.ModelAdmin):
    """
       Manage Albums
       To-Do: Add managing photos from admin section
    """
    search_fields = ["title"]
    list_display = ["title"]

class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
    """
       Admin section for Image class
    """
    list_display = ["__unicode__", "title", "user", "size", "thumbnail", "tags_", "albums_"]
    list_filter = ["tags", "albums", "user"]
    fieldsets = [
        (None, {'fields': ['image', 'title', 'user']}),
        ('Albums and tags', {'fields': ['tags', 'albums']})
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)