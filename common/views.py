from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Common
from .serializers import CommonSerializer
from rest_framework import generics
from .models import Common


class CommonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Common.objects.all()
    serializer_class = CommonSerializer

class CommonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Common.objects.all()
    serializer_class = CommonSerializer
    lookup_field = 'id'