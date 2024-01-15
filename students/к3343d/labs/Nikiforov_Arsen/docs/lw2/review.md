# Модель Review

Модель Review содержит отзывы о турах. Она включает в себя следующие поля:

    tour: Связь с моделью Tour через внешний ключ, указывающий на тур, к которому относится отзыв.
    user: Связь с моделью User через внешний ключ, указывающий на пользователя, оставившего отзыв.
    review_date: Дата создания отзыва (автоматически устанавливается при создании записи).
    text: Текст отзыва.
    rating: Рейтинг отзыва в диапазоне от 1 до 10.

```python
from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_date = models.DateField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])

    def __str__(self):
        return f"{self.user.username} - {self.tour.title} - {self.review_date}"
```