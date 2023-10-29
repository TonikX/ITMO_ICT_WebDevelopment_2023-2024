from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.name} in {self.city}'


class Room(models.Model):
    TYPE_ROOM = (
        ("PREMIUM", "premium"),
        ("DELUXE", "deluxe"),
        ("SUITE", "suite"),
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=10, choices=TYPE_ROOM)
    cost = models.IntegerField()
    guest = models.ManyToManyField(User, through='Booking')

    def __str__(self):
        return self.type


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rating = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.user} оn {self.room}'
