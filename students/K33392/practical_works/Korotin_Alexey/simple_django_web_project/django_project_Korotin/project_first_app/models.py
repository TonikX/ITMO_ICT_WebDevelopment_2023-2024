from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class CarOwner(AbstractUser):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    birth_date = models.DateTimeField(null=True)
    passport = models.CharField(max_length=10, null=True)
    home_Address = models.CharField(max_length=200, null=True)
    nationality = models.CharField(max_length=100, null=True)
    owner = models.ManyToManyField(Car, through='Ownership')


class Ownership(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True)


class DriverLicense(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()