# coding=utf-8
from django.db import models
from django.conf import settings
from django.utils.encoding import force_unicode
from PIL import Image

class Album(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, verbose_name='Краткий формат для url')
    summary = models.TextField(blank=True, verbose_name='Описание для альбома')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return force_unicode("%s %s" % (self.name, self.summary))

class Photo(models.Model):
    title = models.CharField(max_length=256)
    summary = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos')
    album = models.ForeignKey(Album)
    is_cover_photo = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s %s' % (self.title, self.summary)

    def get_image_filename(self):
        return '%s%s' % (settings.MEDIA_ROOT, self.image, )

    def get_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image, )

    """    def save(self):
        if self.is_cover_photo:
            other_cover_photo = Photo.objects.filter(album=self.album).filter(is_cover_photo = True)
            for photo in other_cover_photo:
                photo.is_cover_photo = False
                photo.save()
        filename = self.get_image_filename()
        if not filename == '':
            img = Image.open(filename)
            img.thumbnail((512,512), Image.ANTIALIAS)
            img.save(self.get_medium_filename())
            img.thumbnail((150,150), Image.ANTIALIAS)
            img.save(self.get_small_filename())
        super(Photo, self).save()
        """

    def delete(self):
        filename = self.get_image_filename()
        try:
            os.remove(self.get_medium_filename())
            os.remove(self.get_small_filename())
        except:
            pass
        super(Photo, self).delete()

    def get_cover_photo(self):
        if self.photo_set.filter(is_cover_photo=True).count() > 0:
            return self.photo_set.filter(is_cover_photo=True)[0]
        elif self.photo_set.all().count() > 0:
            return self.photo_set.all()[0]
        else:
            return None