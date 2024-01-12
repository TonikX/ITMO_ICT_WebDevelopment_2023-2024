from django.contrib.auth.models import User
from django.db import models

class Guest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    passport = models.CharField(unique=True, max_length=15)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)


class Room(models.Model):
    room_number = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()

    class Meta:
        unique_together = ('hotel', 'room_number')


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    price = models.PositiveIntegerField()


class Feedback(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    text = models.TextField(null=False)
    rate = models.IntegerField()
    author = models.CharField(max_length=30)
