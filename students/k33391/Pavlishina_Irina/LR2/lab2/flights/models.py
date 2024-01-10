from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Passenger(AbstractUser):
    passport = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.passport}"


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class AirLine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class PlaneModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"


class Seat(models.Model):
    plane = models.ForeignKey('flights.PlaneModel', related_name='plane_seats', on_delete=models.CASCADE)
    row = models.CharField(max_length=2)
    column = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.row}{self.column}"


class Flight(models.Model):
    FLIGHT_TYPES = models.TextChoices('type_of', ['arrive', 'departure'])

    flight_number = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    plane = models.ForeignKey("PlaneModel", related_name="plane_flights", on_delete=models.CASCADE)
    departure_city = models.ForeignKey(
        "flights.City", on_delete=models.CASCADE, related_name="%(class)s_departure_city"
    )
    arrival_city = models.ForeignKey(
        "flights.City", on_delete=models.CASCADE, related_name="%(class)s_arrival_city"
    )
    air_line = models.ForeignKey("flights.AirLine", on_delete=models.CASCADE)

    type = models.CharField(max_length=20, choices=FLIGHT_TYPES.choices)
    gate = models.CharField(max_length=10)


class Reservation(models.Model):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_reservations', on_delete=models.CASCADE)
    flight = models.ForeignKey('flights.Flight', related_name='flight_reservations', on_delete=models.CASCADE)
    seat = models.OneToOneField('flights.Seat', related_name='reserved_by', on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=100)


class Comment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    #date_time = models.DateTimeField(auto_now_add=True)
