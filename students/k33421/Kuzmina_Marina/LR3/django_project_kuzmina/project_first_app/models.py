from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(null=True)  # needed that for creating a superuser
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    cars = models.ManyToManyField('Car', through='Ownership')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='drivers',
        related_query_name='driver'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='drivers',
        related_query_name='driver'
    )

class DriverLicence(models.Model):
    owner = models.ForeignKey('Driver', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    licence_type = models.CharField(max_length=10)
    date_of_release = models.DateTimeField()


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)
    drivers = models.ManyToManyField('Driver', through='Ownership')

class Ownership(models.Model):
    car = models.ForeignKey('Car', null=True, on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', null=True, on_delete=models.CASCADE)
    date_beginning = models.DateField()
    date_end = models.DateField()