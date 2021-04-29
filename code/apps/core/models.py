from django.db import models
from sorl.thumbnail import ImageField
from ckeditor_uploader.fields import RichTextUploadingField
from django_extensions.db.fields import AutoSlugField
from slugify import slugify


class SeoModel (models.Model):
    seo_title = models.CharField(max_length=200, blank=True, null=True, default=None)
    seo_description = models.TextField(max_length=400, blank=True, null=True, default=None)
    og_image = ImageField(upload_to='images/opengraph', blank=True, null=True, default=None, verbose_name="SEO Opengraph Image")

    class Meta:
        abstract = True


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    # description = models.TextField(max_length=1200, verbose_name="Описание", blank=True, null=True)
    # image = ImageField(upload_to='images/pages', default='no-image.png', verbose_name="Картинка в шапке", blank=True, null=True)
    slug = AutoSlugField(populate_from='title', slugify_function=slugify, editable=True, null=True)
    published = models.BooleanField(default=True)
    my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=False)
    parent = models.ForeignKey('Page', blank=True, null=True, default=None, related_name='child_pages', verbose_name="Родительская страница", on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title


class PageBlock(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    # description = models.TextField(max_length=1200, verbose_name="Описание", blank=True, null=True)
    # image = ImageField(upload_to='images/pages', default='no-image.png', verbose_name="Картинка в шапке")
    content_html = RichTextUploadingField(blank=True, null=True, default=None, verbose_name="Контент HTML")
    # published = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='title', slugify_function=slugify, editable=True, null=True)
    button = models.SlugField(editable=True, null=True, blank=True, default=None,)
    my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=False)
    page = models.ForeignKey('Page', blank=True, null=True, default=None, related_name='blocks', verbose_name="Страница", on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Price(SeoModel):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    price = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=False)
    my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=False)

    def __str__(self):
        return self.title
