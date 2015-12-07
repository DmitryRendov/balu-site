import re
import uuid
from string import join

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from album.models import Album, Image, Tag
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE



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
    description = HTMLField(_('room description'), max_length=2048, blank=True, null=True)
    #description = models.TextField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), max_length=2048, blank=True, null=True)
    real_size = models.CharField(_('real or maximal size'),max_length=1, choices=ROOM_SIZES)
    square = models.DecimalField(_('room square'), max_digits=4, decimal_places=2, default="0")
    REQUIRED_FIELDS = ['name', 'real_size', 'square']
    album = models.ManyToManyField(Album, blank=True)

    class Meta:
		abstract = True


# Create your models here.
class RealRoom(Room):
    """
    Class implements Rooms

    Real rooms
    """
    is_lux = models.BooleanField(_('lux'), default=False,
                                   help_text=_('Designates whether this room is lux or general kind of room'))
    is_available = models.BooleanField(_('available'), default=True,
                                    help_text=_(
                                        'Designates whether this room is available for booking or not'))

    # Room gallery goes here
    # Room prices goes here

    class Meta(Room.Meta):
        db_table = 'real_rooms'
        verbose_name = _('room')
        verbose_name_plural = _('rooms')
        ordering = ['real_size']

    def get_full_name(self):
        full_name = '%s (%s)' % (self.name, self.real_size)
        return full_name.strip()

    def get_short_name(self):
        return self.name

    def __unicode__(self):
        return self.name

class VirtualRoom(Room):
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
    real_room = models.ForeignKey(RealRoom,
                                   help_text=_('Real room connected to this virtual room'))
    virt_size = models.CharField(_('Virtual room size'), max_length=4, choices=VIRTUAL_ROOM_SIZES)
    featured = models.BooleanField(_('featured'), default=False,
                                   help_text=_('To show this room on main page'))

    kids_allowed = models.SmallIntegerField(_('How many kids are allowed to be as a guest'), default="2")
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    # Custom gallery goes here
    # Custom Price goes here
    class Meta(Room.Meta):
        db_table = 'virtual_rooms'
        ordering = ['virt_size']

    def __unicode__(self):
        return self.name

    def get_full_name(self):
        full_name = '%s (%s)' % (self.real_room.name, self.virt_size)
        return full_name.strip()

    def get_short_name(self):
        return self.real_room.name

    def is_available_(self):
        return bool(self.real_room.is_available)

