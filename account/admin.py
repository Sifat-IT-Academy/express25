from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Foydalanuvchi haqida ko'proq ma'lumot ko'rsatish
    list_display = ('email', 'username', 'is_courier', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_courier', 'gender')
    search_fields = ('email', 'username')
    
    # Foydalanuvchi yaratish formati
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'gender', 'birth_date', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Courier Status', {'fields': ('is_courier',)}),
    )
    
    # Superfoydalanuvchi yaratish formati
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'is_courier')}
        ),
    )
    
    ordering = ('email',)

# Ro'yxatdan o'tkazamiz
admin.site.register(User, UserAdmin)
#salom 