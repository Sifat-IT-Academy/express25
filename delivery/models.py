# Aminjon, Azizbek

from django.db import models
from django.utils import timezone

class Delivery(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('D', 'Delivered'),
        ('C', 'Cancelled'),
    ]
    
    order_id = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=255)
    delivery_address = models.TextField()
    delivery_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Delivery for {self.customer_name} - Order {self.order_id}'

    class Meta:
        ordering = ['-delivery_date']
        verbose_name_plural = 'Deliveries'

# Aminjon, Azizbek

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]
    
    customer_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.customer_name} for {self.product_name}'

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Reviews'
