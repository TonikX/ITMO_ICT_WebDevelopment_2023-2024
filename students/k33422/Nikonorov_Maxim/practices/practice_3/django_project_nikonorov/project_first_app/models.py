from django.db import models
from django.contrib.auth.models import AbstractUser

class CarOwner(AbstractUser):
    LastName = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=30)
    DateOfBirth = models.DateField(null=True, blank=True)
    PassportNumber = models.CharField(max_length=30, null=True)
    Address = models.CharField(max_length=100, null=True)
    Nationality = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return 'owner ' + self.LastName + ' ' + self.FirstName

class Car(models.Model):
    Number = models.CharField(max_length=15)
    Brand = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)
    Colour = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return self.Brand + ' ' + self.Model
    
class Ownership(models.Model):
    carowner = models.ForeignKey('CarOwner', null=True, on_delete=models.CASCADE, related_name='onwerships')
    car = models.ForeignKey('Car', null=True, on_delete=models.CASCADE, related_name='onwerships')
    BeginDate = models.DateField()
    EndDate = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.car) + ' | ' + str(self.carowner)
    
class DriversLicense(models.Model):
    carowner = models.ForeignKey('CarOwner', on_delete=models.CASCADE, related_name='licenses')
    No = models.CharField(max_length=10)
    Type = models.CharField(max_length=10)
    IssueDate = models.DateField()
    
    def __str__(self):
        return self.Type + ' | ' + str(self.carowner)