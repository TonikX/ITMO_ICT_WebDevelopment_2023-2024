from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    passport = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.passport}"


class AirLine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"


class PlaneModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rows = models.IntegerField()
    columns = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Flight(models.Model):
    name = models.CharField(max_length=9)
    status = models.CharField(max_length=30)
    gate = models.CharField(max_length=10)
    date_time = models.DateTimeField()

    plane = models.ForeignKey("PlaneModel", on_delete=models.CASCADE)
    departure_city = models.ForeignKey(
        "City", on_delete=models.CASCADE, related_name="%(class)s_departure_city"
    )
    arrival_city = models.ForeignKey(
        "City", on_delete=models.CASCADE, related_name="%(class)s_arrival_city"
    )
    air_line = models.ForeignKey("AirLine", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.departure_city.name}-{self.arrival_city.name}"


class Ticket(models.Model):
    seat = models.CharField(max_length=10)

    passenger = models.ForeignKey("User", on_delete=models.CASCADE)
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passenger.first_name}-{self.passenger.last_name} {self.seat}"


class Comment(models.Model):
    message = models.CharField(max_length=200)

    date_time = models.DateTimeField(auto_now_add=True)
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
