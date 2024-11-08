from .views import AddressDetailView,AddressListAPIView,PlasticCardDetailView,PlasticCardListAPIView
from django.urls import path


urlpatterns = [
    path('address/<int:id>', AddressDetailView.as_view(), name='address-detail-api'),
    path('addresses/', AddressListAPIView.as_view(), name='address-list-api'),
    path('plastic-card/<int:id>', PlasticCardDetailView.as_view(), name='plastic-card-detail-api'),
    path('plastic-cards/', PlasticCardListAPIView.as_view(), name='plastic-card-list-api'),
]