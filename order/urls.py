from django.urls import path
from .views import (
    OrderListView, OrderDetailView, OrderDeleteView,
    OrderUpdateView, OrderPartialUpdateView, PaymentCreateView
)

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:id>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:id>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('orders/<int:id>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:id>/partial-update/', OrderPartialUpdateView.as_view(), name='order_partial_update'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment_create'),
]
