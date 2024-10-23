from django.contrib import admin
from .models import Delivery
from .models import Review

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'delivery_date', 'status')
    list_filter = ('status', 'delivery_date')
    search_fields = ('order_id', 'customer_name', 'delivery_address')
    ordering = ('-delivery_date',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('customer_name', 'product_name', 'review_text')
    ordering = ('-created_at',)
