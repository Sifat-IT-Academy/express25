from django.shortcuts import redirect
from store.models import Category, Subcategory, Product,Restaurant  
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from store.serializers import StoreSerializer, SubcategorySerializer, ProductSerializer,RestaurantSerializer

# store
class StorePaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Category.objects.all()
    lookup_field = 'id'
    
class StoreListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(category_type='Store')
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # restaurant
class RestaurantPagination(PageNumberPagination):
    page_size = 10  # Har bir sahifada 10 ta element ko'rsatiladi
    page_size_query_param = 'page_size'
    max_page_size = 100

class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'


# category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.filter(category_type='Store')
    serializer_class = StoreSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# subcategory
class SubcategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SubcategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# product
class ProductPagination(PageNumberPagination):
    page_size = 10  # Har bir sahifada 10 ta mahsulot ko'rsatiladi
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]