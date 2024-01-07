from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    registration_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.registration_number})"


class CarOwner(AbstractUser):
    passport_number = models.CharField(max_length=15, null=True)
    home_address = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)
    cars = models.ManyToManyField(
        Car,
        through="Ownership",
        through_fields=("owner", "car"),
        related_name="owners",
    )

    class Meta:
        verbose_name = "Car Owner"
        verbose_name_plural = "Car Owners"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Ownership(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "Ownership"
        verbose_name_plural = "Ownerships"

    def __str__(self):
        return f"{self.owner} owns {self.car} from {self.start_date} to {self.end_date}"


class DrivingLicense(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()

    class Meta:
        verbose_name = "Driving License"
        verbose_name_plural = "Driving Licenses"

    def __str__(self):
        return f"License {self.license_number} for {self.owner}"
