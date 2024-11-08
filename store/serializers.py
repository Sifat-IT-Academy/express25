from rest_framework import serializers
from store.models import Category,Subcategory,Product
from common.serializers import AddressSerializer


class StoreSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)


    class Meta:
        model = Category
        fields =  "__all__"
    

    def validate(self, data):
        phone_number = data.get("phone_number")
        if Category.objects.filter(phone_number=phone_number):
            raise serializers.ValidationError("Bu telefon nomerdan Dokon yaratilgan")


        return super().validate(data)
    


    


    def validate_phone_number(self, value):
        if Category.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("This phone number is already associated with another store.")
        return value
    
    
    
    
class SubcategorySerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')  
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Subcategory
        fields = [
            'id', 'name', 'description', 'category', 'category_name', 'image'
        ]

    def validate_category(self, value):
        if not value:
            raise serializers.ValidationError("Subcategory must be linked to a valid Category.")
        return value
    
class ProductSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.ReadOnlyField(source='subcategory.name')  

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'subcategory',
            'subcategory_name', 'image', 'stock'
        ]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value