from django.conf.urls import url, include
from . import views
from rest_framework import routers
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import generics


router = routers.DefaultRouter()
router.register(r'albums', views.GalleryAlbumViewSet, 'albums')

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(router.urls)),
]
