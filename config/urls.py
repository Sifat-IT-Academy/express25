from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from common.views import AddressViewSet, PlasticCardViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from delivery.views import (
    DeliveryListView, DeliveryStatusView, ReviewCreateView
)
from order.views import (
    OrderCreateView, OrderListView, OrderDetailView, 
    PaymentCreateView,)


schema_view = get_schema_view(
    openapi.Info(
        title="Express 25",
        default_version='v1',
        description="Restaurants and Stores delivery service",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="express25@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)





# Define routers
router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'plastic-cards', PlasticCardViewSet, basename='plasticcard')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/store/',include('store.urls'),name='store-api' ),
    path('api/v1/delivery/',include('delivery.urls')),
    
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('payments/', PaymentCreateView.as_view(), name='payment-create'),
    path('deliveries/', DeliveryListView.as_view(), name='delivery-list'),
    path('deliveries/<int:pk>/', DeliveryStatusView.as_view(), name='delivery-status'),
    path('deliveries/<int:pk>/review/', ReviewCreateView.as_view(), name='review-create'),

    path('addresses/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name='address-detail'),
    path('plastic-cards/<int:pk>/', PlasticCardViewSet.as_view({'get': 'retrieve' ,'put':'update','patch':'partial_update','delete':'destroy'}), name='plastic-card-detail'),
    path('api/account/',include('accaunt.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]