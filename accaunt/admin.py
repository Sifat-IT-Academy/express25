from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Courier

class CourierAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle_type', 'availability')
    search_fields = ('user__phone_number', 'vehicle_type')
    list_filter = ('availability',)


admin.site.register((User,Courier))