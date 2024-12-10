from rest_framework import generics, status
from rest_framework.response import Response
from order.models import Order, ProductOrder,Payment
from order.serializers import OrderSerializer, OrderDetailSerializer,PaymentSerializer
from rest_framework.permissions import IsAuthenticated
from order.permissons import IsOrderOwner
from rest_framework.exceptions import PermissionDenied


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        for product in serializer.validated_data['product_orders']:
            ProductOrder.objects.create(order=order, **product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated, IsOrderOwner]


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.validated_data['order']
        if order.customer != self.request.user:
            raise PermissionDenied("Siz bu buyurtma uchun to‘lovni amalga oshira olmaysiz.")
        serializer.save()