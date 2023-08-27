from django.contrib import admin
from .models import Room, Address, Reservation, Hotel


# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'room_number']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('status',)
