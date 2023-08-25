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
    # nested serializer
    address = AddressSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    reservation = ReservationSerializer(read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='hotel-detail')
    rooms = serializers.HyperlinkedIdentityField(many=True, view_name='rooms-detail')

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'is_active', 'create_date', 'detail', 'rooms']

