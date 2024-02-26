from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.utils import timezone


class User(AbstractUser):
    user_barcode = models.CharField(max_length=14, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    experience = models.FloatField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(50.0)])
    passport = models.CharField(max_length=12)

    REQUIRED_FIELDS = ['user_barcode', 'last_name', 'first_name', 'experience', 'passport']


class Item(models.Model):
    measurement_units = (
        ('kg', 'kilogram'),
        ('p', 'piece'),
        ('ml', 'milliliters')
    )

    item_barcode = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=50)
    measurement_unit = models.CharField(max_length=2, choices=measurement_units, default='kg')

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    old_warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='old_shipments')
    new_warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='new_shipments')
    amount = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    datetime = models.DateTimeField(default=timezone.now)


class Nomenclature(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0, validators=[MinValueValidator(0.0)])


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    label = models.CharField(max_length=25, blank=True)
    main_text = models.CharField(max_length=3000, blank=True)
