from django.db import models

from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.contrib.auth import get_user_model

class CarOwner(AbstractUser):
    passport = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True)
    cars = models.ManyToManyField('Car', through='CarOwnership')
    birth_date = models.DateField(null=True)

    class Meta:
        ordering = ['id']

class Car(models.Model):
    gov_number = models.CharField(max_length=15)
    car_make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True, through='CarOwnership')

    def __str__(self):
        return f'{self.gov_number} {str(self.model)}'

    class Meta:
        ordering = ['id']


class DriversLicence(models.Model):
    owner_car = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    licence_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    given_at = models.DateField()

    def __str__(self):
        return f'{self.licence_number} of {self.owner_car}'

    class Meta:
        ordering = ['id']

class CarOwnership(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_begin = models.DateField()
    date_end = models.DateField(null=True)

    def __str__(self):
        return f'{self.car} of {self.owner}'

    class Meta:
        ordering = ['id']

