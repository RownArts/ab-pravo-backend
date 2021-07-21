from rest_framework import serializers
from django.conf import settings
from .models import *

# from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
# from abpravo_project.utils import build_absolute_img_url, build_frontend_url


class GalleryVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GalleryVideo
        fields = ('id', 'video_page_link', 'title')
        # fields = '__all__'


class GalleryPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GalleryPhoto
        fields = ('id', 'image', 'title')
        # fields = '__all__'


class GalleryAlbumSerializer(serializers.ModelSerializer):
    videos = GalleryVideoSerializer(read_only=True, many=True)
    photos = GalleryPhotoSerializer(read_only=True, many=True)

    class Meta:
        model = GalleryAlbum
        fields = '__all__'
