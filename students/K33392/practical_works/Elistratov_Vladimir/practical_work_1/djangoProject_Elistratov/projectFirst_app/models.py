from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings

# Create your models here.


class Car(models.Model):
    colors = [
        ("Red", "Red"),
        ("Green", "Green"),
        ("Blue", "Blue"),
        ("Pink", "Pink"),
        ("Orange", "Orange"),
        ("Grey", "Grey"),
        ("White", "White"),
        ("Black", "Black"),
        ("Other", "Unknown")
    ]
    govNumber = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=10, choices=colors)


class CarOwner(AbstractUser):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    bornDate = models.DateField()

    owningCars = models.ManyToManyField(Car, through='Treaty')

    homeAddress = models.CharField(max_length=150, blank=False)
    nationality = models.CharField(max_length=15, blank=False)
    passportNumber = models.CharField(max_length=7)
    passportSubNumber = models.CharField(max_length=5)


class Treaty(models.Model):
    carOwnerID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    carID = models.ForeignKey(Car, on_delete=models.PROTECT)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()


class OwnerDocument(models.Model):
    carOwnerID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()
