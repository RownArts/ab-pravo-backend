from django.db import models
from sorl.thumbnail import ImageField
from django.utils import timezone
# from ckeditor_uploader.fields import RichTextUploadingField
from django_extensions.db.fields import AutoSlugField
from slugify import slugify


class GalleryAlbum(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    # summary = models.TextField(max_length=800, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', slugify_function=slugify, editable=False, null=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    published = models.BooleanField(default=True)
    my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['my_order']
        verbose_name = "Фото альбом"
        verbose_name_plural = "Фото альбомы"


class GalleryPhoto(models.Model):
    image = ImageField(upload_to='images/gallery/%Y/%m/', default='no-image.png')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    album = models.ForeignKey('GalleryAlbum', blank=True, null=True, default=None, related_name='photos', on_delete=models.SET_NULL)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    published = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)+'. ' + str(self.image)


class GalleryVideo(models.Model):
    video_page_link = models.URLField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Подпись к видео')
    album = models.ForeignKey('GalleryAlbum', blank=True, null=True, default=None, related_name='videos', on_delete=models.SET_NULL)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    published = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)+'. ' + str(self.video_page_link)
