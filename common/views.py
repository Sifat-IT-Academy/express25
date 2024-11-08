from django.shortcuts import render
from rest_framework import generics
from .serializers import AddressSerializer,PlasticCardSerializer
from .models import Address,PlasticCard

class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address
    lookup_field = 'id'

    
class AddressListAPIView(generics.ListCreateAPIView):
    queryset = Address.objects.filter()
    serializer_class = AddressSerializer


class PlasticCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlasticCardSerializer
    queryset = PlasticCard
    lookup_field = 'id'

    
class PlasticCardListAPIView(generics.ListCreateAPIView):
    queryset = PlasticCard.objects.filter()
    serializer_class = PlasticCardSerializer
