from rest_framework.permissions import BasePermission

class IsOrderOwner(BasePermission):
    """
    Faqat buyurtma egasi yoki administrator ko‘ra oladi.
    """
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user or request.user.is_staff
