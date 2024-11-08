from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/store/',include('store.urls'),name='store-api' ),
    path('api/v1/address/',include('common.urls'),name='common-api'),
    path('api/v1/plastic-card/',include('common.urls'),name='common-api'),
    path('api/v1/delivery/',include('delivery.urls'),name='delivery-api'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
