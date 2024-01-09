from django.db import models


class Owner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)


class Car(models.Model):
    registration_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)


class DrivingLicense(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='driving_license')
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='ownership')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='ownership')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
