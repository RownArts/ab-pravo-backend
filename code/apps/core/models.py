from django.db import models
from sorl.thumbnail import ImageField
from ckeditor_uploader.fields import RichTextUploadingField
from django_extensions.db.fields import AutoSlugField
from slugify import slugify
from django.utils import timezone


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
        ordering = ['my_order']
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=200)
    smi_name = models.CharField(max_length=200, blank=True, null=True, default=None)
    link = models.CharField(max_length=200)
    # image = ImageField(upload_to='images/pages', default='no-image.png', verbose_name="Картинка в шапке", blank=True, null=True)
    slug = AutoSlugField(populate_from='title', slugify_function=slugify, editable=False, null=True)
    published = models.BooleanField(default=True)
    # my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=False)
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['created_date']
        verbose_name = "СМИ"
        verbose_name_plural = "СМИ"

    def __str__(self):
        return self.title


class PageBlock(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    # description = models.TextField(max_length=1200, verbose_name="Описание", blank=True, null=True)
    image = ImageField(upload_to='images/pageblock', blank=True, null=True, default=None)
    content_html = RichTextUploadingField(blank=True, null=True, default=None, verbose_name="Контент HTML")
    # published = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='title', slugify_function=slugify, editable=True, null=True)
    # button = models.SlugField(editable=True, null=True, blank=True, default=None,)
    my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=False)
    page = models.ForeignKey('Page', blank=True, null=True, default=None, related_name='blocks', on_delete=models.SET_NULL)

    class Meta(object):
        ordering = ['my_order']
        verbose_name = "Блок страницы"
        verbose_name_plural = "Блоки страниц"

    def __str__(self):
        return self.title


class Button(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    href = models.CharField(max_length=100, editable=True, null=True, blank=True, default=None,)
    my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=False)
    # published = models.BooleanField(default=True)
    block = models.ForeignKey('PageBlock', blank=True, null=True, default=None, related_name='buttons', on_delete=models.SET_NULL)\


    class Meta(object):
        verbose_name = "Кнопка"
        verbose_name_plural = "Кнопки"

    def __str__(self):
        return self.title


class Price(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    price = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=False)
    published = models.BooleanField(default=True)

    class Meta(object):
        ordering = ['my_order']
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

    def __str__(self):
        return self.title


class SiteConfig(models.Model):
    key = models.SlugField(max_length=200)
    phone1 = models.CharField(max_length=200, blank=True, null=True, default=None)
    phone2 = models.CharField(max_length=200, blank=True, null=True, default=None)
    whatsapp = models.CharField(max_length=200, blank=True, null=True, default=None)
    email = models.CharField(max_length=200, blank=True, null=True, default=None)
    address = models.CharField(max_length=200, blank=True, null=True, default=None)
    contacts_text = models.CharField(max_length=200, blank=True, null=True, default=None)
    vk = models.CharField(max_length=200, blank=True, null=True, default=None)
    ig = models.CharField(max_length=200, blank=True, null=True, default=None)

    def __str__(self):
        return self.key

    class Meta(object):
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"


class Comment(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    role = models.CharField(max_length=200, blank=False, null=False, verbose_name="Должность")
    content = models.TextField(max_length=200, verbose_name="Текст отзыва")
    image = ImageField(upload_to='images/comments', default='no-image.png', blank=True, null=True, verbose_name="Изображение")
    slug = AutoSlugField(populate_from='name', slugify_function=slugify, editable=False, null=True)
    published = models.BooleanField(default=True, verbose_name="Публикация")
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    # my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, editable=False)

    class Meta:
        ordering = ['created_date']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    name = models.CharField(max_length=200)
    sender = models.CharField(max_length=200, blank=False, null=False)
    # message = models.CharField(max_length=200, blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name
