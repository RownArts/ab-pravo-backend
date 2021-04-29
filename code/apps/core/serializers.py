from rest_framework import serializers
from django.conf import settings
from apps.core.models import *

# from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
# from abpravo_project.utils import build_absolute_img_url, build_frontend_url


class PageBlocksSerializer(serializers.ModelSerializer):

    # def get_content_html(self, obj):
    #     return (build_absolute_img_url(self, obj.content_html))

    class Meta:
        model = PageBlock
        fields = '__all__'


class PageShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = '__all__'
        # fields = ('seo_title', 'seo_description', 'og_image', 'slug',)


class PageSerializer(serializers.ModelSerializer):
    blocks = PageBlocksSerializer(read_only=True, many=True)
    # child_pages = PageShortSerializer(read_only=True, many=True)

    class Meta:
        model = Page
        fields = '__all__'


class PriceShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = '__all__'
