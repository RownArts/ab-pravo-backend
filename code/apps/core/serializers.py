from rest_framework import serializers
from django.conf import settings
from apps.core.models import *
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

# from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
# from abpravo_project.utils import build_absolute_img_url, build_frontend_url


class ButtonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Button
        fields = '__all__'


class PageBlocksSerializer(serializers.ModelSerializer):
    buttons = ButtonSerializer(read_only=True, many=True)
    original = serializers.ImageField(source='image')

    # def get_content_html(self, obj):
    #     return (build_absolute_img_url(self, obj.content_html))

    class Meta:
        model = PageBlock
        fields = '__all__'

    thumbnail = HyperlinkedSorlImageField(
        '512x512',
        options={"quality": 85},
        source='image',
        read_only=True
    )


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


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    avatar = HyperlinkedSorlImageField(
        '256x256',
        options={"crop": "center", "quality": 85},
        source='image',
        read_only=True
    )


class SiteConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteConfig
        fields = '__all__'
