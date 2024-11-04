from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, ProductOrder, Payment
from .serializers import OrderSerializer, ProductOrderSerializer, PaymentSerializer

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

class OrderDeleteView(APIView):
    def delete(self, request, id, format=None):
        order = get_object_or_404(Order, id=id)
        order_id = order.id
        order.delete()
        return Response({'message': f'Order "{order_id}" has been successfully deleted.'}, status=status.HTTP_200_OK)

class OrderUpdateView(APIView):
    def put(self, request, id, format=None):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Order "{order.id}" has been successfully updated.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderPartialUpdateView(APIView):
    def patch(self, request, id, format=None):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Order "{order.id}" has been partially updated.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentCreateView(APIView):
    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Payment created successfully.', 'payment_id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
