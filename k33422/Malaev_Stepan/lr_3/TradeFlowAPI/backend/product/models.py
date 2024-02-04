import datetime

from django.db import models

from backend.manufacturer.models import Manufacturer
from backend.utils.models import (
    AbstractTimeStampedModel,
)


class Product(AbstractTimeStampedModel):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    unique_code = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    weight = models.FloatField()
    production_date = models.DateField()
    warranty_period = models.IntegerField()
    measurement_unit = models.CharField(max_length=50)
    
    def is_expired(self):
        expiry_date = self.production_date + datetime.timedelta(days=self.warranty_period)
        return timezone.now().date() > expiry_date
    
    def __str__(self):
        return f"{self.name} {self.weight} {self.measurement_unit}"


class ProductBatch(AbstractTimeStampedModel):
    batch_number = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_conditions = models.CharField(max_length=200)
    delivery_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.batch_number} {self.product}"
