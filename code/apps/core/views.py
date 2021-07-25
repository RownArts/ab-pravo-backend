# from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
# from django.views.decorators.vary import vary_on_cookie


class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.filter(published=True)
    lookup_field = 'slug'

    def get_queryset(self):
        return Page.objects.filter(published=True)

    @method_decorator(cache_page(settings.CACHETIME_CUSTOM))
    # @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PriceViewSet(viewsets.ModelViewSet):
    serializer_class = PriceSerializer
    queryset = Price.objects.filter(published=True)

    def get_queryset(self):
        return Price.objects.filter(published=True)

    @method_decorator(cache_page(settings.CACHETIME_CUSTOM))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SiteConfigViewSet(viewsets.ModelViewSet):
    serializer_class = SiteConfigSerializer
    queryset = SiteConfig.objects.all()
    lookup_field = 'key'

    @method_decorator(cache_page(settings.CACHETIME_CUSTOM))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.filter(published=True)

    def get_queryset(self):
        return Publication.objects.filter(published=True)

    @method_decorator(cache_page(settings.CACHETIME_CUSTOM))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(published=True)

    def get_queryset(self):
        return Comment.objects.filter(published=True)

    @method_decorator(cache_page(settings.CACHETIME_CUSTOM))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def api_create_contact_view(request):
    sender = 'server@ab-pravo.ru'
    send_to_email = 'info@ab-pravo.ru'
    if request.method == "POST":
        serializer = ContactSerailizer(data=request.data)
        if serializer.is_valid():
            name = request.data.get("name")
            contact = request.data.get("email")

            # send mail
            send_mail(
                'Contact Form mail from site' + sender,
                name + '. ' + contact,
                sender,
                [send_to_email],
            )
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
