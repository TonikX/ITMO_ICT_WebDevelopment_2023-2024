from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Passenger(AbstractUser):
    passport = models.CharField(max_length=100, blank=True, null=True)


class Flight(models.Model):
    FLIGHT_TYPES = models.TextChoices('arrival', 'departure')
    flight_number = models.CharField(max_length=100)
    airline = models.CharField(max_length=100)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=FLIGHT_TYPES.choices)
    gate = models.CharField(max_length=10)


class Seat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=100)
    date = models.DateTimeField()


class Comment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
