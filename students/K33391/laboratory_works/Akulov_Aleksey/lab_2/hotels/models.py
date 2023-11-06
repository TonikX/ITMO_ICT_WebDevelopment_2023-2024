from django.db import models
from django.contrib.auth.models import AbstractUser


class Visitor(AbstractUser):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True, blank=True)
    passport = models.CharField(max_length=25, null=True)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    owner_contact = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    amenities = models.ManyToManyField(Amenity, related_name='room_types', blank=True)


class Reservation(models.Model):
    user = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Reservation {self.user} - {self.id}'


class Review(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    stay_from = models.DateField()
    stay_to = models.DateField()
    author = models.ForeignKey(Visitor, on_delete=models.CASCADE)

