from rest_framework import serializers
from .models import Delivery

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__' 

    def validate(self, data):
        if not Delivery.objects.exists():
            raise serializers.ValidationError("Zakaz qilish uchun avval ro'yhatdan o'tishingiz kerak")
        
        return data
