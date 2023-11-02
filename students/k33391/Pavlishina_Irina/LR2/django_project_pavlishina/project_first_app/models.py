from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CarOwner(AbstractUser):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField(blank=True, null=True)

    passport = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    home_address = models.CharField(max_length=100, blank=True, null=True)

class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Ownership")


class License(models.Model):
    id = models.IntegerField(primary_key=True)
    CarOwner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='licenses', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_given = models.DateField()


class Ownership(models.Model):
    id = models.IntegerField(primary_key=True)
    CarOwner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner_cars', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='car_owners', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
