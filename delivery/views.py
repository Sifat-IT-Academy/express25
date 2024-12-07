from rest_framework import generics, status
from rest_framework.response import Response
from delivery.models import Review, Delivery
from delivery.serializers import DeliverySerializer, ReviewSerializer

class DeliveryListView(generics.ListAPIView):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        return Delivery.objects.filter(order__customer=self.request.user)

class DeliveryStatusView(generics.RetrieveAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

