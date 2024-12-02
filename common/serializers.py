from rest_framework import serializers
from datetime import datetime
from common.models import Address,PlasticCard
from accaunt.serializers import RegisterSerializer

class PlasticCardSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = PlasticCard
        fields = "__all__"
    def validate(self, attrs):
        card_number = attrs.get('card_number')
        expiration_date = attrs.get('expiration_date')

        if not card_number.isdigit() or len(card_number) != 16:
            raise serializers.ValidationError({
                'card_number': "Karta raqami haqiqiy 16 xonali raqam bo'lishi kerak."
            })

        try:
            expiration = datetime.strptime(expiration_date, "%m/%y")
        except ValueError:
            raise serializers.ValidationError({
                'expiration_date': "Yaroqlilik muddati MM/YY formatida bo'lishi kerak."
            })

        if expiration < datetime.now():
            raise serializers.ValidationError({
                'expiration_date': "Ushbu kartaning amal qilish muddati tugagan va uni ishlatib bo'lmaydi."
            })
        return attrs
    def create(self, validated_data):
        request = self.context.get('request')  
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user 
        return super().create(validated_data)
        


class AddressSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Address
        fields = "__all__"
        
    def create(self, validated_data):
        request = self.context.get('request')  
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user 
        return super().create(validated_data)

