from django.contrib import admin
from .models import Room, Address, Reservation, Hotel
# Register your models here.


admin.site.register(Room)
admin.site.register(Address)
admin.site.register(Reservation)
admin.site.register(Hotel)
