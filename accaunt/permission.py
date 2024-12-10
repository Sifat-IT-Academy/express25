from rest_framework.permissions import BasePermission

class IsCourier(BasePermission):
    """
    Faqat kuryerlar uchun ruxsat.
    """
    def has_permission(self, request, view):
        # Foydalanuvchi autentifikatsiya qilinganligini va kuryer ekanligini tekshirish
        return request.user and request.user.is_authenticated and request.user.is_courier