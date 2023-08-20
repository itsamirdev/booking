from enum import Enum

from django.db import models


# Create your models here.

class RoomStatus(models.TextChoices):
    APPROVED = "APPROVED",
    PENDING = "PENDING",
    COMPLETED = "COMPLETED",
    CANCELLED = "CANCELLED"


class Room(models.Model):
    bed_count = models.IntegerField()
    is_empty = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=RoomStatus.choices)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.id


class Address(models.Model):
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=16, unique=True)
    postal_code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)


class Reservation(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=16, unique=True)
    national_code = models.IntegerField(unique=True)
    price = models.IntegerField()
    reservation_date = models.DateField()
    reservation_days = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)

