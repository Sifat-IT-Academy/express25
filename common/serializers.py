from rest_framework import serializers
from common.models import Address,PlasticCard
from accaunt.models import User

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields =  "__all__"


class PlasticCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlasticCard
        fields =  "__all__"