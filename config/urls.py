from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from common.views import AddressViewSet, PlasticCardViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView


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
    

    path('addresses/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name='address-detail'),
    path('plastic-cards/<int:pk>/', PlasticCardViewSet.as_view({'get': 'retrieve' ,'put':'update','patch':'partial_update','delete':'destroy'}), name='plastic-card-detail'),
    path('api/account/',include('accaunt.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]