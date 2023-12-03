from django.db import models


class CarOwner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class License(models.Model):
    LICENSE_TYPE = (
        ('B', 'passenger car'),
        ('C', 'truck'),
        ('D', 'bus'),
    )
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.IntegerField()
    type = models.CharField(max_length=2, choices=LICENSE_TYPE)
    date_of_issue = models.DateField()


class Car(models.Model):
    license_plate_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owner = models.ManyToManyField(CarOwner, through='Ownership')

    def __str__(self):
        return self.license_plate_number


class Ownership(models.Model):
    user = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)

