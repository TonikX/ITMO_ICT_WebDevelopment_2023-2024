from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# class User(AbstractUser):
#     pass
class User(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    passport = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class License(models.Model):
    LICENSE_TYPE = (
        ('B', 'passenger car'),
        ('C', 'truck'),
        ('D', 'bus'),
    )
    car_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    license_number = models.IntegerField()
    type = models.CharField(max_length=2, choices=LICENSE_TYPE)
    date_of_issue = models.DateField()


class Car(models.Model):
    license_plate_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owner = models.ManyToManyField(get_user_model(), through='Ownership')

    def __str__(self):
        return self.license_plate_number


class Ownership(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
