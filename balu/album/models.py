import os
import sys
from django.db import models
from loginsys.models import User
from string import join
from PIL import Image as PImage
from django.conf import settings
from django.core.files import File
from os.path import join as pjoin
from tempfile import *
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

reload(sys)
sys.setdefaultencoding('utf-8')

class Album(models.Model):
    title = models.CharField(_('Album name'), max_length=60)
    public = models.BooleanField(_('Is it public?'), default=False)
    description = HTMLField(_('Album description'), max_length=2048, blank=True, null=True)

    class Meta:
        db_table = 'albums'
        verbose_name = _('album')
        verbose_name_plural = _('albums')
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')

    def get_poster(self):
        posters = [x for x in self.image_set.all() if not x.is_poster]
        posters_lst = ["<img class='media-object' src='/media/%s' alt='%s'>" % (x.image, x.title) for x in posters]
        return join(posters_lst, '')

    images.allow_tags = True


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    class Meta:
        db_table = 'tags'
        verbose_name = _('tags')
        verbose_name_plural = _('tags')
        ordering = ['tag']

    def __unicode__(self):
        return self.tag


class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images/")
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)
    is_poster = models.BooleanField(_('poster'), default=False,
                                   help_text=_('It is a poster for the whole album?'))
    thumb128 = models.ImageField(upload_to="images/", blank=True, null=True)
    thumb64 = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        db_table = 'images'
        verbose_name = _('image')
        verbose_name_plural = _('images')
        ordering = ['title']

    def __unicode__(self):
        return self.image.name

    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)

    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(join(lst, ', '))

    def albums_(self):
        lst = [x[1] for x in self.albums.values_list()]
        return str(join(lst, ', '))

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
            (self.thumb64.name, self.thumb64.name))

    thumbnail.allow_tags = True

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(pjoin(settings.MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size

        # large thumbnail
        fn, ext = os.path.splitext(self.image.name)
        im.thumbnail((128,128), PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb2" + ext
        tf2 = NamedTemporaryFile()
        im.save(tf2.name, "JPEG")
        self.thumb128.save(thumb_fn, File(open(tf2.name)), save=False)
        tf2.close()

        # small thumbnail
        im.thumbnail((64,64), PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb" + ext
        tf = NamedTemporaryFile()
        im.save(tf.name, "JPEG")
        self.thumb64.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()

        super(Image, self).save(*args, ** kwargs)