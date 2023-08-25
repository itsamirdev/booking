from django.db import models

from accounts.models import User


# Create your models here.

class RoomStatus(models.TextChoices):
    READY = "READY",
    UNDER_REPAIR = "UNDER_REPAIR",
    RESERVED = "RESERVED",
    Inaccessible = "Inaccessible"


class Room(models.Model):
    bed_count = models.IntegerField()
    status = models.CharField(max_length=12, choices=RoomStatus.choices, default=RoomStatus.READY)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class Address(models.Model):
    hotel_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=16, unique=True)
    postal_code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.hotel_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    rooms = models.ManyToManyField(to=Room)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.hotel_name} | active:{self.is_active}'


class ReservationStatus(models.TextChoices):
    APPROVED = "APPROVED",
    PENDING = "PENDING",
    FAILED = "FAILED",
    CANCELLED = "CANCELLED"


class Reservation(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ReservationStatus.choices, default=ReservationStatus.PENDING)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=16, unique=True)
    national_code = models.CharField(max_length=16, unique=True)
    Hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    reservation_date = models.DateField()
    reservation_days = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name.username
