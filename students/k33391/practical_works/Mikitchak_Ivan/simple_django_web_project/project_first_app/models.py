from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Owner(AbstractUser):
	last_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	birth_date = models.DateField(null=True, blank=True)
	passport_number = models.CharField(max_length=30, null=True, blank=True)
	home_address = models.CharField(max_length=60, null=True, blank=True)
	nationality = models.CharField(max_length=30, null=True, blank=True)


class Car(models.Model):
	state_number = models.CharField(max_length=15)
	brand = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	color = models.CharField(max_length=30, null=True, blank=True)


class DriverLicense(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	license_number = models.CharField(max_length=10)
	type = models.CharField(max_length=10)
	issue_date = models.DateField()


class Ownership(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	since_date = models.DateField()
	till_date = models.DateField(null=True, blank=True)
