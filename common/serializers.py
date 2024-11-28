from rest_framework import serializers
from .models import Address, PlasticCard
from datetime import date
from accaunt.serializers import RegisterSerializer


class AddressSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)  # Display user as read-only

    class Meta:
        model = Address
        fields = "__all__"
        read_only_fields = ['user']  # Ensure user is read-only

    def create(self, validated_data):
        request = self.context.get('request')  # Access request from serializer context
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user  # Set the user to the logged-in user
        return super().create(validated_data)


class PlasticCardSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)  # Display user as read-only

    class Meta:
        model = PlasticCard
        fields = "__all__"
        read_only_fields = ['user']  # Ensure user is read-only

    def validate(self, data):
        expiration_date = data.get("expiration_date")
        if expiration_date and expiration_date < date.today():
            raise serializers.ValidationError("Kartaning amal qilish muddati tugagan.")
        return super().validate(data)

    def create(self, validated_data):
        request = self.context.get('request')  
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user  
        return super().create(validated_data)
