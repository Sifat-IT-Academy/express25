from django.urls import path
from .views import OrderCreateView, PaymentUpdateView, ProductOrderView

urlpatterns = [
#     path('orders/', OrderCreateView.as_view({'put': 'create'}), name='order-list'),
#     path('payments/', PaymentUpdateView.as_view({'put': 'create'}), name='payment-list'),
#     path('product-orders/', ProductOrderView.as_view({'get': 'list','put': 'update', 'patch':'create','delete': 'destroy'}), name='product-order-list'),
 ]
