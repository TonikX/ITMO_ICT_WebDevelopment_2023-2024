from django.db import models


class Owner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birthday = models.DateField(blank=True, null=True)


class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type_CH = ('A', 'B', 'C', 'D', 'E')
    type = models.CharField(choices=zip(type_CH, type_CH), max_length=1)
    issue_date = models.DateField()


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_until = models.DateField(blank=True, null=True)

