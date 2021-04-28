from django.contrib import admin
from apps.core.models import *
from adminsortable2.admin import SortableAdminMixin
# for image thumbnails
from sorl.thumbnail.admin import AdminImageMixin
# from sorl.thumbnail import get_thumbnail
# from django.utils.safestring import mark_safe
import nested_admin


# class PageBlockInline(nested_admin.NestedTabularInline):
class PageBlockInline(nested_admin.NestedStackedInline):
    model = PageBlock
    # exclude = ('my_order', 'published', )
    # inlines = [PromoButtonInline]
    extra = 0


@admin.register(Page)
# class PageAdmin(AdminImageMixin, admin.ModelAdmin):
class PageAdmin(SortableAdminMixin, AdminImageMixin, nested_admin.NestedModelAdmin):

    ordering = ('my_order',)
    # list_display = ['title', 'image_tag', 'parent', 'published', ]
    # list_display_links = ['title', 'image_tag', ]
    # list_filter = ('published', 'parent',)

    # def image_tag(self, obj):
    #     thumb = get_thumbnail(obj.image, '256x256')
    #     return mark_safe('<img src="{url}" height="64" /></div>'.format(url=thumb.url,))

    pass


@admin.register(PageBlock)
class PageBlockAdmin(SortableAdminMixin, AdminImageMixin, admin.ModelAdmin):

    ordering = ('my_order',)
    pass


@admin.register(Price)
class PriceAdmin(SortableAdminMixin, AdminImageMixin, admin.ModelAdmin):

    ordering = ('my_order',)
    pass
