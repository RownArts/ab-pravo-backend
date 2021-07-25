from django.conf.urls import url, include
from . import views
from rest_framework import routers
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import generics


router = routers.DefaultRouter()
router.register(r'pages', views.PageViewSet, 'pages')
router.register(r'prices', views.PriceViewSet, 'prices')
router.register(r'publications', views.PublicationViewSet, 'publications')
router.register(r'comments', views.CommentViewSet, 'comments')
router.register(r'prices', views.PriceViewSet, 'prices')
router.register(r'site-configs', views.SiteConfigViewSet, 'site-configs')

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/post-contacts', views.api_create_contact_view),
]
