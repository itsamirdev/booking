from django.db import models

from accounts.models import User


# Create your models here.

class RoomStatus(models.TextChoices):
    READY = "READY",
    PENDING = "PENDING",
    RESERVED = "RESERVED",
    CANCELLED = "CANCELLED"


class Room(models.Model):
    bed_count = models.IntegerField()
    status = models.CharField(max_length=10, choices=RoomStatus.choices, default=RoomStatus.READY)
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


class Reservation(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, unique=True)
    national_code = models.IntegerField(unique=True)
    reservation_date = models.DateField()
    reservation_days = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name.username


class Hotel(models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.create_date} | {self.is_active}'
