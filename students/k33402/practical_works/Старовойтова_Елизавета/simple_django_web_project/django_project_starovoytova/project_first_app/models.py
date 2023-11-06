from django.db import models


# Create your models here.


class Car(models.Model):
    id_car = models.IntegerField(primary_key=True)
    gos_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)


class Owner(models.Model):
    id_owner = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday_date = models.DateTimeField(null=True)


class Ownership(models.Model):
    id_owner_car = models.IntegerField()
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField(null=True)


class DriverLicense(models.Model):
    id_license = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    num_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateTimeField()

