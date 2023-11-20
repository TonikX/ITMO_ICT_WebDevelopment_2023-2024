# Модель TourReservation

Модель TourReservation:

Модель TourReservation представляет собой информацию о бронировании туров. Она включает следующие поля:

    tour: Связь с моделью Tour через внешний ключ, указывающий на тур, который был забронирован.
    user: Связь с моделью User через внешний ключ, указывающий на пользователя, сделавшего бронирование.
    is_confirmed: Флаг, указывающий на подтверждение бронирования.
    
```python
from django.db import models
from django.contrib.auth.models import User

class TourReservation(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
```