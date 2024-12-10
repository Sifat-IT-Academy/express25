from rest_framework import generics
from rest_framework.response import Response
from delivery.models import Review, Delivery
from order.models import Order
from delivery.serializers import DeliverySerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from accaunt.permission import IsCourier  # Custom permission (Kurierlar uchun)
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

class CreateDeliveryView(APIView):
    permission_classes = [IsAuthenticated, IsCourier]  # Faqat kuryerlar uchun

    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        try:
            # Zakazni olish
            order = Order.objects.get(id=order_id)

            # Zakaz uchun yetkazib berish mavjudligini tekshirish
            if hasattr(order, 'delivery'):
                raise ValidationError("Bu zakaz uchun yetkazib berish allaqachon mavjud.")

            # Yetkazib berishni yaratish
            delivery = Delivery.objects.create(
                order=order,
                courier=request.user,
                delivery_time=timezone.now()
            )

            # Zakaz statusini yangilash
            order.status = 'processing'
            order.save()

            return Response({
                "message": "Yetkazib berish yaratildi.",
                "delivery_id": delivery.id
            })

        except Order.DoesNotExist:
            return Response({"error": "Zakaz topilmadi."}, status=404)
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)