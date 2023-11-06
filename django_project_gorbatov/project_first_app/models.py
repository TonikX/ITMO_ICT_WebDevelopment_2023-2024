from django.db import models

class Car(models.Model):
    id_car = models.IntegerField(primary_key=True)
    state_number = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

class Owner(models.Model):
    id_owner = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birth_day = models.DateTimeField(null=True)

class Own(models.Model):
    id_car_owner = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True)

class License(models.Model):
    id_license = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateTimeField()