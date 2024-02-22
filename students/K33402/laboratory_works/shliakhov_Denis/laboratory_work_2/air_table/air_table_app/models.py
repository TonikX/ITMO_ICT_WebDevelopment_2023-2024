from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Passenger(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{str(self.first_name).capitalize()} {str(self.last_name).capitalize()}"


class Flight(models.Model):
    class Type(models.TextChoices):
        DEPARTURE = "DEPARTURE"
        ARRIVAL = "ARRIVAL"

    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=100)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    type = models.CharField(max_length=20, choices=Type)
    gate = models.CharField(max_length=20)


class Seat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    row_number = models.IntegerField()
    col_name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.row_number}{self.col_name}".upper()


class Reservation(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.ticket_number}"


class Comment(models.Model):
    class Rating(models.IntegerChoices):
        TERRIBLE = 1
        BAD = 2
        OK = 3
        GOOD = 4
        EXCELLENT = 5

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=Rating)
