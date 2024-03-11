from django.contrib.auth.models import User
from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.CharField(max_length=100)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    gate_number = models.CharField(max_length=10)
    flight_type = models.CharField(max_length=10)


class AppUser(User):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)


class Reservation(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="reservations")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="reservations")


class Review(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField()
    rating = models.IntegerField()
    commenter = models.ForeignKey(AppUser, on_delete=models.CASCADE)
