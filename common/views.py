from rest_framework import viewsets, permissions
from .serializers import AddressSerializer, PlasticCardSerializer
from .models import Address, PlasticCard

class PlasticCardViewSet(viewsets.ModelViewSet):
    serializer_class = PlasticCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PlasticCard.objects.filter(user=self.request.user)


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
