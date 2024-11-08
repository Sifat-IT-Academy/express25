from rest_framework import serializers
from store.models import Category
from common.serializers import AddressSerializer



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  "__all__"
            

    def validate(self, data):
        phone_number = data.get("phone_number")
        if Category.objects.filter(phone_number=phone_number):
            raise serializers.ValidationError("Bu telefon nomerdan Dokon yaratilgan")


        return super().validate(data)
    


    



