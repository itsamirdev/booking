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
    class Meta:
        model = Hotel
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    # rooms = serializers.HyperlinkedIdentityField(many=True, view_name='rooms-detail')

    class Meta:
        model = Hotel
        fields = ['name', 'is_active', 'created_at']


class HotelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
