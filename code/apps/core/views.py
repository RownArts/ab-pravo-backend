# from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import permissions
from apps.core.models import *
from apps.core.serializers import *
# from django.shortcuts import get_object_or_404
# from django_filters import rest_framework as DjangoFilterBackend
# from django_filters.rest_framework import DjangoFilterBackend
# from telos_project.pagination import CustomPagination

# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import ensure_csrf_cookie
# for banners random
# import random
# import re

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.filter(published=True)
    lookup_field = 'slug'

    def get_queryset(self):
        return Page.objects.filter(published=True)

    @method_decorator(cache_page(settings.CACHETIME_CUSTOM))
    @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PriceViewSet(viewsets.ModelViewSet):
    serializer_class = PriceSerializer
    queryset = Price.objects.filter(published=True)

    def get_queryset(self):
        return Price.objects.filter(published=True)

    @method_decorator(cache_page(settings.CACHETIME_CUSTOM))
    @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
