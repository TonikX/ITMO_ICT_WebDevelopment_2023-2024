# Модель Reservation

Модель Reservation содержит информацию о бронировании тура пользователями. Включает следующие поля:

    user: Связь с моделью User через внешний ключ, указывающий на пользователя, сделавшего бронирование.
    tour: Связь с моделью Tour через внешний ключ, указывающий на тур, который был забронирован.
    reservation_date: Дата создания записи о бронировании (автоматически устанавливается при создании записи).
    is_confirmed:

```python
from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.tour.title}"
```