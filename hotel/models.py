from django.db import models

from accounts.models import User


# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.name} | active:{self.is_active}'


class Address(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=16, unique=True)
    postal_code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.hotel.name} | {self.postal_code}'


class RoomStatus(models.TextChoices):
    READY = "READY",
    UNDER_REPAIR = "UNDER REPAIR",
    RESERVED = "RESERVED",
    INACCESSIBLE = "INACCESSIBLE"


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    bed_count = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=12, choices=RoomStatus.choices, default=RoomStatus.READY)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    room_number = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class ReservationStatus(models.TextChoices):
    APPROVED = "APPROVED",
    PENDING = "PENDING",
    FAILED = "FAILED",
    CANCELLED = "CANCELLED"


class Reservation(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ReservationStatus.choices, default=ReservationStatus.PENDING)
    reservation_date = models.DateField()
    reservation_days = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name.username)
