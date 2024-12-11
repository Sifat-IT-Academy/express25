from django.urls import path
from delivery.views import (
    DeliveryListView,
    DeliveryStatusView,
    ReviewCreateView,
    CreateDeliveryView,
)

urlpatterns = [
    path('deliveries/', DeliveryListView.as_view(), name='delivery-list'),  
    path('deliveries/<int:pk>/', DeliveryStatusView.as_view(), name='delivery-detail'),
    path('deliveries/create/', CreateDeliveryView.as_view(), name='create-delivery'), 
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),  
]
