from django.db import models

from accounts.models import User


# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.flight_number} - {self.departure_airport} to {self.arrival_airport}"


class Gender(models.TextChoices):
    MALE = "MALE",
    FEMALE = "FEMALE",
    OTHER = "OTHER",


class Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=Gender.choices)
    nationality = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | {self.gender}"


class PaymentStatus(models.TextChoices):
    PENDING = "PENDING",
    COMPLETED = "COMPLETED",
    FAILED = "FAILED",
    REFUNDED = "REFUNDED",


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    is_confirmed = models.BooleanField(default=False)
    reservation_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)

    def __str__(self):
        return f"{self.passenger} - {self.flight}"
