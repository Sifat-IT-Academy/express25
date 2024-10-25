from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name', 'descriptions',]

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=['name', 'category',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'price',]

