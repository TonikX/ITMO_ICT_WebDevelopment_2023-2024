from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Driver(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    passport = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=30, null=True)
    cars = models.ManyToManyField("Car", through="Ownership")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    drivers = models.ManyToManyField("Driver", through="Ownership")

    def __str__(self):
        return f"{self.number} {self.brand} {self.model}"


class Ownership(models.Model):
    car = models.ForeignKey(
        "Car", null=True, on_delete=models.CASCADE, related_name="ownership"
    )
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="ownership",
    )
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.car.number} {self.driver.first_name}"


class DriverLicense(models.Model):
    driver = models.ForeignKey(
        "Driver", on_delete=models.CASCADE, related_name="license"
    )
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    creation_date = models.DateField()

    def __str__(self):
        return f"{self.number} {self.driver.first_name}"
