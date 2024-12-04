from django.contrib import admin
from .models import Order, ProductOrder, Payment

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'courier', 'status', 'total_price', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('customer__username', 'courier__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('customer', 'courier')


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    list_filter = ('order', 'product')
    search_fields = ('order__id', 'product__name')
    ordering = ('order',)
    autocomplete_fields = ('order', 'product')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'method', 'status')
    list_filter = ('status', 'method')
    search_fields = ('order__id', 'amount')
    ordering = ('-id',)
    autocomplete_fields = ('order',)
