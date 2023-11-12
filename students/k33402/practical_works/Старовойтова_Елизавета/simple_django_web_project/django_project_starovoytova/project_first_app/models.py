from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    gos_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=15)
    home_address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=30)
class Owner(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    id_owner = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday_date = models.DateTimeField(null=True)
    cars = models.ManyToManyField(Car, through='Ownership')

class Ownership(models.Model):
    id_owner_car = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField(null=True)

class DriverLicense(models.Model):
    id_license = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    num_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateTimeField()
