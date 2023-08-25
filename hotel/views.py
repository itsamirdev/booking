# from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Hotel, Reservation, Room
from .serializers import HotelSerializer, HotelListSerializer, ReservationSerializer, RoomSerializer


# Create your views here.

class HotelView(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filterset_fields = ['rooms__status', 'address__hotel_name']
    search_fields = ['name', 'address__hotel_name']
    ordering_fields = ['-create_date']


class HotelDetailView(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelReservation(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class HotelRoomsView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

