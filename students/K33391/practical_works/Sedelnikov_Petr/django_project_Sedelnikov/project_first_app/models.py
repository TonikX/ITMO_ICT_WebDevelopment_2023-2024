from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CarOwner(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birthday_date = models.DateField(null=True)
    cars = models.ManyToManyField('Car', through="Ownership")
    passport = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    nationality = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DriverLicense(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_id = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()

    def __str__(self):
        return f"{self.license_id} {self.owner_id.first_name} {self.owner_id.last_name}"


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    car_owner = models.ManyToManyField(CarOwner, through='Ownership')

    def __str__(self):
        return f"{self.number} {self.brand} {self.model}"


class Ownership(models.Model):
    car = models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
    car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.car.number} {self.car_owner.first_name}  {self.car_owner.last_name}  {self.start_date} {self.end_date}"
