from django.contrib import admin
# for image thumbnails
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
import nested_admin

from .models import GalleryPhoto, GalleryAlbum, GalleryVideo


class GalleryPhotoInline(admin.TabularInline, AdminImageMixin, nested_admin.NestedStackedInline):
    model = GalleryPhoto
    # exclude = ('show_on_main', )
    extra = 1


class GalleryVideoInline(admin.TabularInline, AdminImageMixin, nested_admin.NestedStackedInline):
    model = GalleryVideo
    # exclude = ('show_on_main', )
    extra = 1


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(AdminImageMixin, nested_admin.NestedModelAdmin, admin.ModelAdmin):
    inlines = [GalleryVideoInline, GalleryPhotoInline]
    list_display = ('title', 'published',)
    list_display_links = ['title', ]
    list_filter = ('published', 'created_date')

    # def image_tag(self, obj):
    #     thumb = get_thumbnail(obj.image, '128x128', crop="center")
    #     return mark_safe('<img src="{url}" height="64" /></div>'.format(url=thumb.url,))

    pass
