from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)


class Owner(AbstractUser):
    passport = models.CharField(max_length=10, default='0000000000')
    address = models.CharField(max_length=50, default='Planet Earth')
    nationality = models.CharField(max_length=30, default='World citizen')
    birthday = models.DateField(blank=True, null=True)
    cars = models.ManyToManyField(Car, through='Ownership')


class License(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type_CH = ('A', 'B', 'C', 'D', 'E')
    type = models.CharField(choices=zip(type_CH, type_CH), max_length=1)
    issue_date = models.DateField()


class Ownership(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_until = models.DateField(blank=True, null=True)

