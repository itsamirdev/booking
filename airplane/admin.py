from django.contrib import admin

from django.contrib import admin
from .models import Airport, Flight, Passenger


# Register your models here.

@admin.register(Airport)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(Flight)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Passenger)
class RoomAdmin(admin.ModelAdmin):
    pass


