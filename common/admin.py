from django.contrib import admin
from .models import PlasticCard, Address


# PlasticCard modelini admin panelda ro'yxatdan o'tkazish
@admin.register(PlasticCard)
class PlasticCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'expiration_date', 'is_active')  # Admin panelda ko'rinadigan ustunlar
    list_filter = ('is_active', 'expiration_date')  # Filter bo'yicha qidiruv
    search_fields = ('user__username', 'card_number')  # Qidiruv maydoni (user modeli bilan bog'langan)

# Address modelini admin panelda ro'yxatdan o'tkazish
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'label', 'city', 'district', 'postal_code')  # Ko'rinadigan ustunlar
    list_filter = ('city', 'district')  # Filter bo'yicha qidiruv
    search_fields = ('user__username', 'city', 'postal_code')  # Qidiruv maydoni


