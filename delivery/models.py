from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils import timezone

class Delivery(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]

    order = models.OneToOneField("order.Order", on_delete=models.CASCADE, related_name='delivery')
    courier = models.ForeignKey("accaunt.User", on_delete=models.CASCADE, related_name='deliveries')
    delivery_time = models.DateTimeField()  # Yetkazib berish boshlanish vaqti
    delivered_at = models.DateTimeField(null=True, blank=True)  # Yetkazib berilgan vaqt
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'
        ordering = ['-delivery_time']

    def clean(self):
        if self.delivered_at and self.delivered_at < self.delivery_time:
            raise ValidationError("Delivery time cannot be earlier than the start time.")
        if self.delivery_time > timezone.now():
            raise ValidationError("Delivery start time cannot be in the future.")

    def __str__(self):
        return f"Delivery {self.id} for Order {self.order.id}"


class Review(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='reviews')
    customer_name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError("Rating must be between 1 and 5.")

    def __str__(self):
        return f"Review for Delivery {self.delivery.id} - Rating: {self.rating}"