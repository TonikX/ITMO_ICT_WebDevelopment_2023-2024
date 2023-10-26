from django.db import models


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField()
    owner = models.ManyToManyField(Car, through='Ownership')


class Ownership(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True)


class DriverLicense(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()