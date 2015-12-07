from django.contrib import admin

# Register your models here.
from .models import Album, Image, Tag

class AlbumAdmin(admin.ModelAdmin):
    """
       Manage Albums
       To-Do: Add managing photos from admin section
    """
    search_fields = ['title']
    list_display = ['title', 'description', 'public']
    list_filter = ['title', 'public']

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']

class ImageAdmin(admin.ModelAdmin):
    '''
       Admin section for Image class
    '''
    list_display = ['__unicode__', 'title', 'user', 'size', 'thumbnail', 'tags_', 'albums_', 'is_poster']
    list_filter = ['tags', 'albums', 'user']
    fieldsets = [
        (None, {'fields': ['image', 'title', 'user']}),
        ('Albums and tags', {'fields': ['tags', 'albums', 'is_poster']})
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)