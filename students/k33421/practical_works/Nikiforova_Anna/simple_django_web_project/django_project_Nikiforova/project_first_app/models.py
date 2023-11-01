from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)  # needed that for creating a superuser
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    cars = models.ManyToManyField('Car', through='Ownership', related_name='owners')


class DriverLicence(models.Model):
    owner = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='driver_licences')
    number = models.CharField(max_length=10)
    licence_type = models.CharField(max_length=10)
    date_of_release = models.DateField()


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)
    drivers = models.ManyToManyField('Driver', through='Ownership', related_name='driver_cars')


class Ownership(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='ownerships')
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='ownerships')
    date_beginning = models.DateField()
    date_end = models.DateField()
