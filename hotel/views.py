# from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Hotel, Reservation, Room
from .serializers import HotelSerializer, HotelListSerializer, ReservationSerializer, RoomSerializer
from rest_framework.response import Response

# Create your views here.


class HotelView(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    # filterset_fields = ['rooms__status', 'address__hotel_name']
    # search_fields = ['name', 'address__hotel_name']
    # ordering_fields = ['-created_at']
    ordering = ['-created_at']


class HotelDetailView(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer


class HotelRoomsView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request, *args, **kwargs):
        hotel_id = self.kwargs.get('pk')
        queryset = Room.objects.filter(hotel_id=hotel_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class HotelReservation(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def list(self, request, *args, **kwargs):
        room_id = self.kwargs.get('pk')
        queryset = Reservation.objects.filter(room_id=room_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

