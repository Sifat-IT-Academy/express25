from django.contrib import admin
from .models import Category, Subcategory, Product

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_type', 'phone_number', 'rating')
    search_fields = ('name', 'category_type')
    list_filter = ('category_type', 'rating')


# Subcategory Admin
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'subcategory', 'stock')
    search_fields = ('name', 'subcategory__name')
    list_filter = ('subcategory', 'price')
