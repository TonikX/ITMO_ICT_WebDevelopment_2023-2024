from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    gov_num = models.CharField(max_length=15, null=False)
    car_mark = models.CharField(max_length=20, null=False)
    car_model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.color} {self.car_mark} {self.car_model} {self.gov_num}"


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    date_of_birth = models.DateTimeField(null=False)

    cars = models.ManyToManyField(
        Car,
        through="Ownership",
        through_fields=("owner_id", "car_id"),
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DriveLicense(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_num = models.CharField(max_length=10, null=False)
    license_type = models.CharField(max_length=10, null=False)
    given_date = models.DateTimeField(null=False)


class Ownership(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    ownership_type = models.CharField(max_length=10, null=False)
    start_date = models.DateField(null=False)
    finish_date = models.DateField(null=False)


class CustomUser(AbstractUser):
    passport_number = models.CharField(max_length=20)
    home_address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=30)
