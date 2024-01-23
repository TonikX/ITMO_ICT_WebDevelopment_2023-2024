import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Owner(AbstractUser):
    last_name = models.CharField(max_length=30, default='')
    first_name = models.CharField(max_length=30, default='')
    birth_date = models.DateTimeField(default=datetime.datetime.now())
    passport_number = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=100, default='')
    nationality = models.CharField(max_length=30, default='')


User = get_user_model()


class Car(models.Model):
    owner = models.ManyToManyField(User, through='Possession')
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Possession(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=None, blank=True, null=True)


class DriverLicense(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()
