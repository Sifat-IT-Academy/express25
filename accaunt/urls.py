from django.urls import path

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlastikViewSet, AddressViewSet

router = DefaultRouter()
router.register(r'plastik', PlastikViewSet, basename='plastik')
router.register(r'address', AddressViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls)),
]