from django.contrib import admin

# Register your models here.
from .models import Room, VirtualRoom

class RoomAdmin(admin.ModelAdmin):
    list_filter = ('name', 'is_available')
    fields = ('name', 'description', ('real_size', 'square'), ('is_lux', 'is_available'))
    list_display = ('name', 'real_size', 'is_available')

    class Meta:
        model = Room

admin.site.register(Room, RoomAdmin)

class VirtualRoomAdmin(admin.ModelAdmin):

    class Meta:
        model = VirtualRoom

admin.site.register(VirtualRoom, VirtualRoomAdmin)