
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/store/',include('store.urls'),name='store-api' ),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
