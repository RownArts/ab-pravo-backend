from django.contrib import admin
from apps.core.models import *
from adminsortable2.admin import SortableAdminMixin
# for image thumbnails
from sorl.thumbnail.admin import AdminImageMixin
# from sorl.thumbnail import get_thumbnail
# from django.utils.safestring import mark_safe
import nested_admin


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    pass


# class PageBlockInline(nested_admin.NestedTabularInline):
class PageBlockInline(nested_admin.NestedStackedInline):
    model = PageBlock
    # exclude = ('my_order', 'published', )
    # inlines = [PromoButtonInline]
    extra = 0


class ButtonInline(nested_admin.NestedTabularInline):
    model = Button
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
    inlines = [PageBlockInline]

    # def image_tag(self, obj):
    #     thumb = get_thumbnail(obj.image, '256x256')
    #     return mark_safe('<img src="{url}" height="64" /></div>'.format(url=thumb.url,))

    pass


@admin.register(PageBlock)
class PageBlockAdmin(SortableAdminMixin, nested_admin.NestedModelAdmin):
    list_display = ['title', 'page', ]
    list_filter = ('page',)
    inlines = [ButtonInline]

    ordering = ('my_order',)
    pass


@admin.register(Price)
class PriceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'published', ]
    list_editable = ['price', 'published', ]

    ordering = ('my_order',)
    pass


@admin.register(Button)
class ButtonAdmin(SortableAdminMixin, nested_admin.NestedModelAdmin):

    ordering = ('my_order',)
    pass


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):

    pass
