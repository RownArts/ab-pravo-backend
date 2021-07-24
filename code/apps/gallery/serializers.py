from rest_framework import serializers
# from django.conf import settings
from .models import *
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

# from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
# from abpravo_project.utils import build_absolute_img_url, build_frontend_url


class GalleryVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GalleryVideo
        fields = ('id', 'video_page_link', 'title')
        # fields = '__all__'


class GalleryPhotoSerializer(serializers.ModelSerializer):
    original = serializers.ImageField(source='image')

    class Meta:
        model = GalleryPhoto
        fields = ('id', 'original', 'thumbnail', 'title')
        # fields = '__all__'

    thumbnail = HyperlinkedSorlImageField(
        '250x100',
        options={"crop": "center", "quality": 85},
        source='image',
        read_only=True
    )


class GalleryAlbumSerializer(serializers.ModelSerializer):
    videos = GalleryVideoSerializer(read_only=True, many=True)
    photos = GalleryPhotoSerializer(read_only=True, many=True)

    class Meta:
        model = GalleryAlbum
        fields = '__all__'
