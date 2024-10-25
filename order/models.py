from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    courier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='courier_orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.total_price < 0:
            raise ValidationError("Total price cannot be negative.")


    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-created_at']


class ProductOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='product_orders')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_orders')
    quantity = models.PositiveIntegerField()

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")


    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.id}"

    class Meta:
        verbose_name = "ProductOrder"
        verbose_name_plural = "ProductOrders"
        unique_together = ('order', 'product')


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def clean(self):
        if self.amount < 0:
            raise ValidationError("Amount cannot be negative.")

        if self.status == 'refunded' and self.order.status != 'completed':
            raise ValidationError("Only completed payments can be refunded.")

    def __str__(self):
        return f"Payment {self.id} for Order {self.order.id} - {self.status}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
