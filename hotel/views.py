from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Hotel
from .serializers import HotelSerializer

# Create your views here.

class HotelView(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
