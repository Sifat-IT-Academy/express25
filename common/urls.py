from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlasticCardViewSet, AddressViewSet


router = DefaultRouter()
router.register(r'plasticcards', PlasticCardViewSet, basename='plasticcard')
router.register(r'addresses', AddressViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls)), 
]
