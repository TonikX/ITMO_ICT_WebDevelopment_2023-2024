from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=300)


class Product(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=300)
    unit = models.CharField(max_length=100)
    shelf_life = models.IntegerField()

    def __str__(self):
        return self.name


class BrokerCompany(models.Model):
    name = models.CharField(max_length=100)
    income = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Broker(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(BrokerCompany, related_name='brokers', on_delete=models.CASCADE)
    income = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Consignment(models.Model):
    broker = models.ForeignKey(Broker, related_name='what_sold', on_delete=models.CASCADE)

    date_sold = models.DateField()
    num = models.CharField(max_length=20)
    cost = models.FloatField()
    prepayment = models.BooleanField()


class ProductByCompany(models.Model):
    company = models.ForeignKey(Company, related_name='what_produced', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='produced_by', on_delete=models.CASCADE)
    consignment = models.ForeignKey(Consignment, related_name='what_in', on_delete=models.CASCADE)
    created = models.DateField()

    def __str__(self):
        return f"{self.product.name} by {self.company.name}"