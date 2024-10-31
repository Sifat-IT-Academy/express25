from rest_framework import serializers
from store.models import Category
from common.serializers import AddressSerializer
from .models import Category, Subcategory



class StoreSerializer(serializers.ModelSerializer):
    # address = AddressSerializer(readonly=True)
    class Meta:
        model = Category
        fields =  "__all__"

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'address', 'phone_number', 'rating']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category', 'description']


