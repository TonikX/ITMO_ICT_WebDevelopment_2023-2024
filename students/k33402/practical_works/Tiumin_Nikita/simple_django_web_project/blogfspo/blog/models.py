from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth = models.DateTimeField(blank=True, null=True)

    cars = models.ManyToManyField('Car', through='CarOwnership')


class DriverLicense(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issued_at = models.DateTimeField()


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)

    owners = models.ManyToManyField(Owner, through='CarOwnership')


class CarOwnership(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(blank=True, null=True)
