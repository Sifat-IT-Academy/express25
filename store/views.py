from store.models import Category
from store.serializers import StoreSerializer
from rest_framework import generics, permissions


class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Category
    lookup_field = 'id'
  
class StoreListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(category_type='Store')
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]