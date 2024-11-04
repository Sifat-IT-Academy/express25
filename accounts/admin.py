from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Ro'yxatdan o'tkazamiz
admin.site.register(User)
#salom 