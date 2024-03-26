from django.db import models

# Create your models here.


class CarOwner(models.Model):
    surname = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=30, null=False)
    birthday = models.DateTimeField(null=True)


class Car(models.Model):
    number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=20, null=False)


class Owning(models.Model):
    id_car_owner = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, null=True)
    id_car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(null=False)
    stop_date = models.DateTimeField(null=True)


class License(models.Model):
    id_car_owner = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, null=True)
    number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date = models.DateTimeField(null=False)
