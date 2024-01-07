from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    USERNAME_FIELD = 'id_driver'
    id_driver = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    username = None

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)
    drivers = models.ManyToManyField(Driver, through="Ownership")


class Ownership(models.Model):
    id_ownership = models.AutoField(primary_key=True)
    car_id = models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class DriverLicence(models.Model):
    id_driver_licence = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()
