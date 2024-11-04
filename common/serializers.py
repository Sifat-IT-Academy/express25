from rest_framework import serializers
from .models import  Address,Common
 
class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common
        fields = '__all__'
        
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
