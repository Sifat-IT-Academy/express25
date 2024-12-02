from rest_framework import serializers
from .models import Order, ProductOrder, Payment
from accaunt.models import User
from store.models import Product 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  
        
class ProductOrderSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = ProductOrder
        fields = ['id', 'order', 'product', 'product_name', 'quantity']

class PaymentSerializer(serializers.ModelSerializer):
    order_id = serializers.ReadOnlyField(source='order.id')

    class Meta:
        model = Payment
        fields = ['id', 'order_id', 'amount', 'method', 'status']

class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    courier = UserSerializer(read_only=True)
    product_orders = ProductOrderSerializer(many=True, read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'customer', 'courier', 'status', 'total_price',
            'created_at', 'updated_at', 'product_orders', 'payments'
        ]
