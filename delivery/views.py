from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Delivery
from .serializers import DeliverySerializer
from rest_framework import generics
from .models import Delivery
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Delivery, Review
from django.core.exceptions import ValidationError                                                                                                      


# class DeliveryListCreateAPIView(APIView):
#     def get(self, request):
#         deliveries = Delivery.objects.all()
#         serializer = DeliverySerializer(deliveries, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = DeliverySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DeliveryDetailAPIView(APIView):
#     def get_object(self, id):
#         return get_object_or_404(Delivery, id=id)

#     def get(self, request, id):
#         delivery = self.get_object(id)
#         serializer = DeliverySerializer(delivery)
#         return Response(serializer.data)

#     def put(self, request, id):
#         delivery = self.get_object(id)
#         serializer = DeliverySerializer(delivery, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         delivery = self.get_object(id)
#         delivery.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class DeliveryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    lookup_field = 'id'


def delivery_list(request):
   
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/delivery_list.html', {'deliveries': deliveries})


def delivery_detail(request, delivery_id):
   
    delivery = get_object_or_404(Delivery, id=delivery_id)
    return render(request, 'delivery/delivery_detail.html', {'delivery': delivery})


def review_create(request, delivery_id):
   
    delivery = get_object_or_404(Delivery, id=delivery_id)
    if request.method == "POST":
        rating = int(request.POST.get('rating', 5))
        comment = request.POST.get('comment', '')

        
        try:
            if rating < 1 or rating > 5:
                raise ValidationError("Rating 1 dan 5 gacha bo'lishi kerak.")
            if len(comment) > 500:
                raise ValidationError("Izoh 500 belgidan oshmasligi kerak.")
            
            # Creating Review
            Review.objects.create(
                delivery=delivery,
                rating=rating,
                comment=comment,
                customer_name=request.POST.get('customer_name', 'Unknown'),
                store_name=request.POST.get('store_name', 'Unknown')
            )
            return redirect('delivery_detail', delivery_id=delivery.id)
        except ValidationError as e:
            return render(request, 'delivery/review_form.html', {
                'delivery': delivery,
                'errors': e.messages
            })
    return render(request, 'delivery/review_form.html', {'delivery': delivery})


def delivery_status_update(request, delivery_id):
    """Update delivery status."""
    delivery = get_object_or_404(Delivery, id=delivery_id)
    if request.method == "POST":
        status = request.POST.get('status', 'pending')
        if status in dict(Delivery.STATUS_CHOICES):
            delivery.status = status
            delivery.save()
            return redirect('delivery_detail', delivery_id=delivery.id)
    return JsonResponse({'error': 'Invalid status'}, status=400)
