from django.db import models


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    cars = models.ManyToManyField('Car', through='Ownership', related_name='ownerships')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=20)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"

class DriverLicense(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20)
    license_type = models.CharField(max_length=50)
    issue_date = models.DateField()

    def __str__(self):
        return f"{self.owner} - {self.license_number}"

class Ownership(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.owner} owns {self.car} ({self.start_date} - {self.end_date})"
