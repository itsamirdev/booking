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
    """
    A view class that handles the listing and creation of reservations.
    """

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def list(self, request, *args, **kwargs):
        """
        Retrieves the flight_id from the URL parameters, filters the reservations based on the flight_id,
        serializes the queryset using the ReservationSerializer, and returns the serialized data as a response.
        """
        flight_id = self.kwargs.get('pk')
        queryset = self.get_queryset().filter(flight_id=flight_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
