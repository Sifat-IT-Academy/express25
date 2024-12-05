from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Order, ProductOrder, Payment
from .serializers import OrderSerializer, ProductOrderSerializer, PaymentSerializer
from .taskss import notify_couriers_task

class OrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            with transaction.atomic():
                order_serializer = OrderSerializer(data=data)
                if order_serializer.is_valid():
                    order = order_serializer.save()

                    # Celery vazifasini ishga tushirish
                    notify_couriers_task.delay(order.id)

                    return Response(order_serializer.data, status=status.HTTP_201_CREATED)
                return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PaymentUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            payment_id = data.get('payment_id')
            new_status = data.get('status')

            payment = Payment.objects.get(id=payment_id)
            payment.status = new_status
            payment.save()

            # Order statusini yangilash
            if new_status == 'completed':
                payment.order.status = 'processing'
            elif new_status == 'failed':
                payment.order.status = 'pending'
            elif new_status == 'refunded':
                payment.order.status = 'cancelled'
            payment.order.save()

            return Response({"message": "Payment and order status updated successfully."}, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
