from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import *
from .serializers import *

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


class GalleryAlbumViewSet(viewsets.ModelViewSet):
    serializer_class = GalleryAlbumSerializer
    queryset = GalleryAlbum.objects.filter(published=True)
    lookup_field = 'slug'

    def get_queryset(self):
        return GalleryAlbum.objects.filter(published=True)

    @method_decorator(cache_page(settings.CACHETIME_CUSTOM))
    @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
