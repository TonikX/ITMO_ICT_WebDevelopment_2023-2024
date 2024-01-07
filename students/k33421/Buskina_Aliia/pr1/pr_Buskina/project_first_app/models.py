
from django.db import models
from django.contrib.auth.models import AbstractUser

class CarOwner(AbstractUser):
    id_owner = models.IntegerField(primary_key=True)
    birth_day = models.DateField(null=True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username

class Car(models.Model):
    id_car = models.IntegerField(primary_key=True)
    state_number = models.CharField(max_length=15, null=False)
    mark_car = models.CharField(max_length=20, null=False)
    model_car = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)
    car_owners = models.ManyToManyField(CarOwner, through='Ownership', related_name='cars')

    def __str__(self):
        return self.state_number

class Ownership(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, related_name="ownerships")
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="ownerships")
    start_date = models.DateField()
    end_date = models.DateField(null=True)

class DriverLicense(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, related_name='licenses')
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date_of_license = models.DateField()
