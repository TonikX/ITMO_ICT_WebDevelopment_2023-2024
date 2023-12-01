from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    passport = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=50, null=True)
    autos = models.ManyToManyField('Auto', through='Ownership')


class Auto(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(null=True, max_length=30)
    drivers = models.ManyToManyField('Driver', through='Ownership')


class OwnerDocs(models.Model):
    driver_id = models.ForeignKey('Driver', on_delete=models.CASCADE)
    docs_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    giving_date = models.DateField()


class Ownership(models.Model):
    driver_id = models.ForeignKey('Driver', null=True, on_delete=models.CASCADE)
    auto_id = models.ForeignKey('Auto', null=True, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField(null=True)