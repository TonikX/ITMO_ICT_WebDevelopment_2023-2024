from django.db import models


class CarOwner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Car(models.Model):
    plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.plate}"

class Ownership(models.Model):
    owner_id = models.ManyToManyField(CarOwner)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class DriverLicence(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    licence_id = models.CharField(max_length=10)
    licence_type = models.CharField(max_length=10)
    recieved_date = models.DateField()

    def __str__(self):
        return f"{self.licence_id}, {self.owner_id}"

