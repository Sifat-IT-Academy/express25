from django.contrib import admin
from .models import PlasticCard, Address

@admin.register(PlasticCard)
class PlasticCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'card_number', 'expiration_date', 'is_active')
    list_filter = ('is_active', 'expiration_date')
    search_fields = ('card_number', 'user__username') 
    ordering = ('-expiration_date',)
    readonly_fields = ('is_active',)  

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'label', 'city', 'district', 'street_adress', 'postal_code')
    list_filter = ('city', 'district')
    search_fields = ('user__username', 'city', 'district', 'street_adress')  
    ordering = ('city',)
