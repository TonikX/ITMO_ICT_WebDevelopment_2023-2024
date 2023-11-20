
# Модель SoldTour

Модель SoldTour отражает информацию о проданных турах. Она содержит следующие поля:

    tour: Связь с моделью Tour через внешний ключ, указывающий на тур, который был продан.
    buyer: Связь с моделью User через внешний ключ, указывающий на покупателя тура.
    sale_date: Дата и время продажи тура (автоматически устанавливается при создании записи).
    price: Цена проданного тура.

```python
from django.db import models
from django.contrib.auth.models import User

class SoldTour(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.buyer.username} - {self.tour.title}"
```