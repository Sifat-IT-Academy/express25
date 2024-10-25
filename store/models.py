from django.core.exceptions import ValidationError
from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='category_images/')
    delivery_time = models.DateField()
    working_time = models.DateField()
    category_type = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def clean(self):
        if self.rating < 0 or self.rating > 5:
            raise ValidationError("Rating must be between 0 and 5.")

    def __str__(self):
        return self.name


# Subcategory Model
class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subcategory_images/')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Subcategories'

    def clean(self):
        if not self.category:
            raise ValidationError("Subcategory must belong to a Category.")

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    stock = models.IntegerField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Products'

    def clean(self):
        if self.price <= 0:
            raise ValidationError("Price must be greater than 0.")
        if self.stock < 0:
            raise ValidationError("Stock cannot be negative.")

    def __str__(self):
        return self.name
