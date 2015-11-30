from django.contrib import admin

# Register your models here.
from .models import RealRoom, VirtualRoom

class RealRoomAdmin(admin.ModelAdmin):
    list_filter = ('name', 'is_available')
    list_display = ('name', 'real_size', 'square', 'is_available')

    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        ('Gallery', {'fields': ['album']}),
        ('Room size', {'fields': ['real_size', 'square']}),
        ('Charachteristics', {'fields': ['is_lux', 'is_available']}),
    ]

    class Meta:
        model = RealRoom

admin.site.register(RealRoom, RealRoomAdmin)

class VirtualRoomAdmin(admin.ModelAdmin):

    list_filter = ('name', 'kids_allowed')
    list_display = ('name', 'virt_size', 'kids_allowed', 'square')

    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        ('Gallery', {'fields': ['album']}),
        ('Real room', {'fields': ['real_room']}),
        ('Room size', {'fields': ['virt_size', 'kids_allowed', 'square']}),
    ]

    class Meta:
        model = VirtualRoom

admin.site.register(VirtualRoom, VirtualRoomAdmin)