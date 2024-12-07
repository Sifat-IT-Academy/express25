from rest_framework import serializers
from order.models import Order, ProductOrder, Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order', 'amount', 'method', 'status']

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    product_orders = ProductOrderSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'total_price', 'created_at', 'product_orders']

class OrderDetailSerializer(serializers.ModelSerializer):
    product_orders = ProductOrderSerializer(many=True)
    payment = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id', 'status', 'total_price', 'created_at', 'product_orders', 'payment']

    def get_payment(self, obj):
        if obj.payment:
            return {
                "amount": obj.payment.amount,
                "method": obj.payment.method,
                "status": obj.payment.status
            }
        return None
