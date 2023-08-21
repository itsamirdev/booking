from rest_framework import serializers
from .models import Hotel, Room, Address, Reservation


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    reservation = ReservationSerializer(read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

