from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Courier

class UserAdmin(BaseUserAdmin):
    model = User

    # Fields to display in the list view
    list_display = ('phone_number', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'gender')

    # Fields to search in the admin panel
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')

    # Ordering of users in the list view
    ordering = ('phone_number',)

    # Define fieldsets for editing a user
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'birth_date', 'gender')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    # Define fieldsets for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'email', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )

    # Enable editing of password from the admin panel
    change_password_form = BaseUserAdmin.change_password_form

class CourierAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle_type', 'availability')
    search_fields = ('user__phone_number', 'vehicle_type')
    list_filter = ('availability',)

# Register the models with the custom admin classes
admin.site.register(User, UserAdmin)
admin.site.register(Courier, CourierAdmin)
