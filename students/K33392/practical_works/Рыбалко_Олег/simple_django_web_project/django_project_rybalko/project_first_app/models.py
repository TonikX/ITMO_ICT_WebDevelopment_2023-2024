from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, ManyToManyField, Model


class CarOwner(AbstractUser):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    date_of_birth = DateTimeField()
    passport_number = CharField(max_length=30)
    home_address = CharField(max_length=50)
    nationality = CharField(max_length=30)


class DriversLicence(Model):
    owner = ForeignKey(CarOwner, CASCADE)
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
