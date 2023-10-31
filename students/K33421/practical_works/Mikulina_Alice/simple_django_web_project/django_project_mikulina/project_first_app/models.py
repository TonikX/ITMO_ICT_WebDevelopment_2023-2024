from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateTimeField(null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    cars = models.ManyToManyField('Car', through='Ownership')

    def __str__(self) -> str:
        return f'{str(self.last_name)} {str(self.first_name)}'

    class Meta:
        ordering = ['id']


class DriverLicense(models.Model):
    owner = models.ForeignKey('Driver', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    licence_type = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.owner} has {str(self.number)} for {self.licence_type}'

    class Meta:
        ordering = ['id']


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30, blank=True, null=True)
    drivers = models.ManyToManyField('Driver', through='Ownership')

    def __str__(self) -> str:
        return f' {str(self.number)} - {str(self.brand)} {str(self.model)} ({str(self.colour)})'

    class Meta:
        ordering = ['id']


class Ownership(models.Model):
    car = models.ForeignKey('Car', null=True, on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', null=True, on_delete=models.CASCADE)
    date_beginning = models.DateField()
    date_end = models.DateField()

    def __str__(self) -> str:
        return f'{self.car} {str(self.driver)} ({self.date_end} - {self.date_end})'

    class Meta:
        ordering = ['id']