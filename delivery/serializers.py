from rest_framework import serializers
from delivery.models import Delivery,Review
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['order', 'courier', 'delivery_time', 'delivered_at', 'status']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['delivery', 'customer_name', 'store_name', 'rating', 'comment', 'created_at']
