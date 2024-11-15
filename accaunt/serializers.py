from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1','password2', 'is_courier', 'gender', 'birth_date')

    def create(self, validated_data):
        password = validated_data.get('password1')
        user = User.objects.create_user(
            email=validated_data.get('email'),
            phone_number=validated_data.get('phone_number'),
            password=password,
            is_courier=validated_data.get('is_courier', False),
            gender=validated_data.get('gender'),
            birth_date=validated_data.get('birth_date')
        )
        return user

    def validate(self, attrs):
       email = attrs.get('email')
       phone_number = attrs.get('phone_number')
       password1 = attrs.get('password1')
       password2 = attrs.get('password2')

       if not email:
           raise serializers.ValidationError('Please enter an email address.')
       try:
            EmailValidator()(email)
       except ValidationError:
           raise serializers.ValidationError('Please enter a valid email address.')

       if User.objects.filter(email=email).exists():
        raise serializers.ValidationError("This email is already registered.")
       
       if not phone_number:
           raise serializers.ValidationError('Please enter your phone number.')

       if password1 != password2:
           raise serializers.ValidationError("Passwords must match.")



       return super().validate(attrs)
class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')

        if phone_number and password:
            user = authenticate(phone_number=phone_number, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
                return user
            raise serializers.ValidationError("Invalid login credentials.")
        raise serializers.ValidationError("Must include 'phone_number' and 'password'.")

from .models import Plastik, Address

class PlastikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plastik
        fields = ['id', 'card_number', 'expiry_date', 'holder_name', 'created_at']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'state', 'postal_code', 'country', 'created_at']
