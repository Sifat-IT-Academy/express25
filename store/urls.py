from .views import StoreDetailView,StoreListAPIView
from django.urls import path

urlpatterns = [
    path('store/<int:id>', StoreDetailView.as_view(), name='store-detail-api'),
    path('stores/', StoreListAPIView.as_view(), name='stores-list-api'),
    


]
