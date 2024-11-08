from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email","username","password","phone_number"]
        extra_kwargs = {
            'password':{'write_only':True}
        }

    
    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        # first_name = validated_data['first_name']
        # last_name = validated_data['last_name']
        password = validated_data['password']
        phone_number = validated_data['phone_number']
        user = get_user_model()
        new_user = user.objects.create(email=email,username=username,phone_number=phone_number)
        new_user.set_password(password)
        new_user.save()
        return new_user
    
    