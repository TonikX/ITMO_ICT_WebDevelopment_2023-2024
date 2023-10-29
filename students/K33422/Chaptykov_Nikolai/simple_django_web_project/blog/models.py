from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=20, default='No address')
    passport = models.CharField(max_length=20, default='No passport')
    nationality = models.CharField(max_length=20, default='No ethnicity')
    birthdate = models.DateField()

    def __str__(self):
        return self.user.username

class PersonAdvanced(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=20, default='No address')
    passport = models.CharField(max_length=20, default='No passport')
    nationality = models.CharField(max_length=20, default='No ethnicity')
    birthdate = models.DateField()

    def __str__(self):
        return self.user.username

class DriverLicense(models.Model):
    driver_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    license_id = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    date_produced = models.DateField()


class Car(models.Model):
    plate_number = models.CharField(max_length=15)
    company_produced = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class OwnerShip(models.Model):
    driver_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_beginning = models.DateField()
    date_end = models.DateField()


class CarsAndPerson(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car)


class ExampleModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Publisher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(self.name, self.publisher)
