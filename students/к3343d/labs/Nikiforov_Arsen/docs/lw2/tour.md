# Модель Tour


Модель Tour представляет собой описание тура. Здесь определены следующие поля:

    title: Название тура.
    agency: Агентство, предоставляющее тур.
    description: Описание тура.
    period: Продолжительность тура.
    payment_conditions: Условия оплаты тура.
    price: Цена тура.
    country: Страна, в которую направлен тур.
```python
from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
    title = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    description = models.TextField()
    period = models.CharField(max_length=50)
    payment_conditions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title
```
