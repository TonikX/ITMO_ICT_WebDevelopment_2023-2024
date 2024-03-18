from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Flight(models.Model):
    class Meta:
        db_table = 'flight'

    class FlightType(models.TextChoices):
        ARRIVAL = 'ARR', 'Arrival'
        DEPARTURE = 'DEP', 'Departure'

    class City(models.TextChoices):
        AMSTERDAM = 'AMS', 'Amsterdam'
        BERLIN = 'BER', 'Berlin'
        COPENHAGEN = 'CPH', 'Copenhagen'
        DUBLIN = 'DUB', 'Dublin'
        HELSINKI = 'HEL', 'Helsinki'
        MOSCOW = 'SVO', 'Moscow (Sheremetyevo)'
        LONDON = 'LHR', 'London (Heathrow)'
        SAINT_PETERSBURG = 'LED', 'Saint-Petersburg (Pulkovo)'

    class Airline(models.TextChoices):
        AEROFLOT = 'AEROFLOT', 'Aeroflot'
        BRIT_AIR = 'BRIT_AIR', 'British Airlines'
        LUFTHANSA = 'LUFTHANSA', 'Lufthansa'
        TURK_AIR = 'TURK_AIR', 'Turkish Airlines'
        AIR_FRANCE = 'AIR_FRANCE', 'Air France'

    flight_number = models.CharField(max_length=16, unique=True)
    airline_name = models.CharField(max_length=32, choices=Airline.choices)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=3, choices=City.choices)
    destination = models.CharField(max_length=3, choices=City.choices)
    type = models.CharField(max_length=9, choices=FlightType.choices)
    gate_number = models.CharField(max_length=8)
    passengers = models.ManyToManyField(User, through='Reservation')


class Reservation(models.Model):
    class Meta:
        db_table = 'reservation'
        unique_together = [['flight', 'seat_number']]
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=4, null=True, blank=True)
    ticket_number = models.CharField(max_length=16, unique=True, null=True, blank=True)
    checked_in = models.BooleanField(default=False)


class Review(models.Model):
    class Meta:
        db_table = 'review'
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(
        default=10,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
