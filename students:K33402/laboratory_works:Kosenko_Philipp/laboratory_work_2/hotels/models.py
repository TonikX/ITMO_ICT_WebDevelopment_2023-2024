from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Passenger(AbstractUser):
    passport = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.passport}"


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"


class TypeOfRoom(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.IntegerField()
    conveniences = models.CharField(max_length=1000)
    cost = models.FloatField()


class Room(models.Model):
    hotel = models.OneToOneField('hotels.Hotel', related_name='rooms', on_delete=models.CASCADE)
    type = models.OneToOneField('hotels.TypeOfRoom', related_name='rooms_of_this_type', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)


class Reservation(models.Model):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_reservations', on_delete=models.CASCADE)
    room = models.ForeignKey('hotels.Room', related_name='reserved_by', on_delete=models.CASCADE)
    date_start = models.DateField()
    date_finish = models.DateField()


class Comment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
