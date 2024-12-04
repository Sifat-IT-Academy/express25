from django.contrib import admin
from .models import Delivery, Review


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'courier', 'delivery_time', 'delivered_at', 'status', 'get_average_rating')
    list_filter = ('status', 'delivery_time')
    search_fields = ('order', 'courier')
    ordering = ('-delivered_at',)
    readonly_fields = ('get_average_rating',)

    def get_average_rating(self, obj):
        return obj.average_rating() or "No Reviews"
    get_average_rating.short_description = "Average Rating"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'store_name', 'delivery', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('customer_name', 'store_name', 'delivery__order')
    ordering = ('-created_at',)
    autocomplete_fields = ('delivery',)
