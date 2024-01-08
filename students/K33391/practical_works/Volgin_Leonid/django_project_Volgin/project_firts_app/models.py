from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

#Create your models here.
class CarOwner(AbstractUser):
    surname = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    cars = models.ManyToManyField('Car', through="Ownership")
    passport = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=30,null=True)
    nationality = models.CharField(max_length=30,null=True)
    def __str__(self):
        return f"{self.first_name} {self.surname}"

class Sertificate(models.Model):
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_sertificate = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_creation = models.DateField()
    def __str__(self):
        return f"{self.number_sertificate} {self.id_owner.first_name} {self.id_owner.surname}"

class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    car_owner = models.ManyToManyField(CarOwner, through='Ownership')
    def __str__(self):
        return f"{self.number} {self.brand} {self.model}"

class Ownership(models.Model):
    car = models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
    car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    date_of_beginning = models.DateField()
    date_of_ending = models.DateField()
    def __str__(self):
        return f"{self.car.number} {self.car_owner.first_name}  {self.car_owner.surname}  {self.date_of_beginning} {self.date_of_ending}"


