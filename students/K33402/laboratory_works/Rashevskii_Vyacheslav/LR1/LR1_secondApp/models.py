from django.db import models
from django.contrib.auth.models import User


class Disks(models.Model):
    prod_date = models.DateField()
    firm = models.CharField(max_length=45)


class Games(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    author = models.CharField(max_length=100)
    disk = models.ForeignKey("Disks", on_delete=models.CASCADE)  # id_disk в бд


class Sale(models.Model):
    sale_date = models.DateField()
    sale_quantity = models.IntegerField()
    disk = models.ForeignKey("Disks", on_delete=models.CASCADE)
    sale_price = models.FloatField()


class Admission(models.Model):
    admission_date = models.DateField()
    admission_quantity = models.IntegerField()
    disk = models.ForeignKey("Disks", on_delete=models.CASCADE)
    admission_price = models.FloatField()


class Sale_point(models.Model):
    sale_point_name = models.CharField(max_length=45)
    sale_point_address = models.CharField(max_length=100)
    number_of_stuff = models.IntegerField()
    sale_id = models.ForeignKey("Sale", on_delete=models.CASCADE)


class Admission_point(models.Model):
    admission_point_name = models.CharField(max_length=45)
    admission_point_address = models.CharField(max_length=100)
    number_of_stuff = models.IntegerField()
    admission_id = models.ForeignKey("Admission", on_delete=models.CASCADE)
