from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, CharField, DateField, DateTimeField, ForeignKey, ManyToManyField, Model


class CarOwner(AbstractUser):
    date_of_birth = DateField(default=date(1970, 1, 1))
    passport_number = CharField(max_length=30, default="")
    home_address = CharField(max_length=50, default="")
    nationality = CharField(max_length=30, default="")


class DriversLicence(Model):
    owner = ForeignKey(CarOwner, CASCADE, related_name="driverslicence")
    number = CharField(max_length=10)
    _type = CharField(max_length=10)
    issue_date = DateTimeField()


class Car(Model):
    number = CharField(max_length=15)
    model = CharField(max_length=20)
    color = CharField(max_length=30)
    owners = ManyToManyField(CarOwner, through="Ownership")


class Ownership(Model):
    owner = ForeignKey(CarOwner, CASCADE)
    car = ForeignKey(Car, CASCADE)
    start_date = DateTimeField()
    end_date = DateTimeField(null=True, blank=True)
