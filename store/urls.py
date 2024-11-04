from .views import StoreDetailView,StoreListAPIView
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Express 25",
        default_version='v1',
        description="Restaruants and Stores delivary service",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="express25gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('store/<int:id>', StoreDetailView.as_view(), name='store-detail-api'),
    path('stores/', StoreListAPIView.as_view(), name='stores-list-api'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
