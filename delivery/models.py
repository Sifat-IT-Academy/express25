from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Delivery(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]
    
    order = models.BigIntegerField()
    courier = models.BigIntegerField()
    delivery_time = models.DateTimeField()  # Yetkazib berish boshlanish vaqti
    delivered_at = models.DateTimeField(null=True, blank=True)  # Yetkazib berilgan vaqt
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    class Meta:
        db_table = 'delivery'
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'
        ordering = ['-delivered_at']

    def __str__(self):
        return f"Delivery {self.id} for Order {self.order}"

    def clean(self):
        """Custom validation for Delivery model."""
        if self.delivered_at:
            if self.delivered_at < self.delivery_time:
                raise ValidationError("Yetkazib berilgan vaqt yetkazib berish boshlanish vaqtidan oldin bo'lishi mumkin emas.")
            if self.delivery_time > timezone.now():
                raise ValidationError("Yetkazib berish boshlanish vaqti kelajakda bo'lishi mumkin emas.")

    def get_status_display(self):
        """Returns the human-readable status."""
        return dict(self.STATUS_CHOICES).get(self.status, "Unknown")

    def average_rating(self):
        """Calculates the average rating for this delivery."""
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(review.rating for review in reviews) / reviews.count(), 2)
        return None


class Review(models.Model):
    customer_name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField(max_length=5)
    comment = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']

    def __str__(self):
        return f"Review for Delivery {self.delivery.id} - Rating: {self.rating}"

    def clean(self):
        """Custom validation for Review model."""
        if self.rating < 1 or self.rating > 5:
            raise ValidationError("Rating 1 dan 5 gacha bo'lishi kerak.")
        if len(self.comment) > 500:
            raise ValidationError("Izoh 500 belgidan oshmasligi kerak.")
