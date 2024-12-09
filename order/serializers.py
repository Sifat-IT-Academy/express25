from rest_framework import serializers
from .models import Order, ProductOrder, Payment
from store.models import Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'created_at', 'updated_at', 'total_price']
        read_only_fields = ['created_at', 'updated_at']

class ProductOrderSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')  # Adding the product name

    class Meta:
        model = ProductOrder
        fields = ['id', 'order', 'product', 'product_name', 'quantity']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'method', 'status']
