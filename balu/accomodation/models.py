import re
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators

## Only for debug
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# end of debug


# Create your models here.
class Room(models.Model):
    """
    Class implements Rooms

    Real rooms
    """
    ROOM_SIZES = (
        ('1', 'One person room'),
        ('2', 'Two persons room'),
        ('3', 'Three persons room'),
        ('4', 'Four persons room'),
    )
    name = models.CharField(_('room name'), max_length=255, blank=True, null=True)
    description = models.TextField(_('room description'), max_length=2048, blank=True, null=True)
    real_size = models.CharField(_('real or maximal size'),max_length=1, choices=ROOM_SIZES)
    square = models.DecimalField(_('room square'), max_digits=4, decimal_places=2, default="0")
    is_lux = models.BooleanField(_('lux'), default=False,
                                   help_text=_('Designates whether this room is lux or general kind of room'))
    is_available = models.BooleanField(_('available'), default=True,
                                    help_text=_(
                                        'Designates whether this room is available for booking or not'))

    # lastupdated = models.DateField(_('Last updated'), auto_now_add=True)
    # Room gallery goes here
    # Room prices goes here

    REQUIRED_FIELDS = ['name', 'real_size', 'square']

    class Meta:
        db_table = 'rooms'
        verbose_name = _('room')
        verbose_name_plural = _('rooms')
        ordering = ['real_size']

    def get_full_name(self):
        full_name = '%s (%s)' % (self.name, self.real_size)
        return full_name.strip()

    def get_short_name(self):
        return self.name

class VirtualRoom(models.Model):
    """
    Class implements Virtual Rooms

    Virtual rooms
    """
    VIRTUAL_ROOM_SIZES = (
        ('1', '1 - Single bed room'),
        ('11', '2 - Two single bed room'),
        ('2', '2 - One double bed room'),
        ('111', '3 - Three single bed room'),
        ('12', '3 - One single and one double bed room'),
        ('1111', '4 - Four single bed room'),
        ('22', '4 - Two double bed room'),
    )
    real_room = models.ForeignKey(Room)
    virt_size = models.CharField(max_length=4, choices=VIRTUAL_ROOM_SIZES)
    kids_allowed = models.SmallIntegerField(_('How many kids are allowed to be as a guest'), default="2")

    # Custom gallery goes here
    # Custom Price goes here

    class Meta:
        db_table = 'virtual_rooms'
        ordering = ['virt_size']

    def get_full_name(self):
        full_name = '%s (%s)' % (self.real_room.name, self.virt_size)
        return full_name.strip()

