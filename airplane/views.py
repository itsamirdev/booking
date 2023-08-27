from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Airport, Flight, Passenger, Reservation
from .serializers import (
    AirportSerializer,
    FlightSerializer,
    PassengerSerializer,
    ReservationSerializer
)


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def list(self, request, *args, **kwargs):
        flight_id = self.kwargs.get('pk')
        queryset = Reservation.objects.filter(flight_id=flight_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
