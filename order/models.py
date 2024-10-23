from django.db import models

# Create your models here.

#Asilbek, Samandar, Bobur
class Category(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500)
    adress = models.TextField()
    phone_number = models.IntegerField()
    rating = models.FloatField()
    image = models.ImageField()
    delivery_time = models.DateField()
    working_time = models.DateField()
    categoty_type = models.CharField(max_length=500)
    pass

class Subcategory(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, models.CASCADE)
    image = models.ImageField()
    pass


class Product(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()
    price = models.IntegerField()
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image = models.ImageField()
    stock = models.CharField(max_length=500)
    pass