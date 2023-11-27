# Модели

### Отель (Hotel)

- Модель `Hotel` представляет собой отель со следующими полями:
  - `name` (CharField): Название отеля (максимальная длина: 200 символов).
  - `owner` (CharField): Владелец отеля (максимальная длина: 100 символов).
  - `address` (TextField): Адрес отеля.
  - `description` (TextField): Описание отеля.
  - `room_types` (TextField): Описание доступных типов номеров.
  - `price` (DecimalField): Цена номеров в отеле (максимальное количество цифр: 10, количество десятичных знаков: 2).
  - `capacity` (PositiveIntegerField): Максимальная вместимость отеля.
  - `amenities` (TextField): Описание удобств в отеле.

```python
  from django.db import models

  class Hotel(models.Model):
      name = models.CharField(max_length=200)
      owner = models.CharField(max_length=100)
      address = models.TextField()
      description = models.TextField()
      room_types = models.TextField()
      price = models.DecimalField(max_digits=10, decimal_places=2)
      capacity = models.PositiveIntegerField()
      amenities = models.TextField()

      def __str__(self):
          return self.name
```

### Бронь (Reservation)

- Модель `Reservation` представляет собой бронирование, сделанное пользователем, со следующими полями:
  - `user` (ForeignKey к модели User): Пользователь, сделавший бронирование.
  - `hotel` (ForeignKey к модели Hotel): Отель, для которого сделано бронирование.
  - `check_in_date` (DateField): Дата заселения в отель.
  - `check_out_date` (DateField): Дата выселения из отеля.
  - `num_guests` (PositiveIntegerField): Количество гостей в бронировании.
  - `additional_notes` (TextField, необязательно): Дополнительные замечания или комментарии к бронированию.

```python
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.PositiveIntegerField()
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Reservation for {self.user.username} at {self.hotel.name}'
```

### Отзыв (Review)

- Модель `Review` представляет собой отзыв пользователя о гостинице со следующими полями:
  - `user` (ForeignKey к модели User): Пользователь, написавший отзыв.
  - `hotel` (ForeignKey к модели Hotel): Гостиница, которую пользователь оценивает.
  - `check_in_date` (DateField, по умолчанию: 1970-01-01): Дата заселения пользователя.
  - `check_out_date` (DateField, по умолчанию: 1970-01-01): Дата выселения пользователя.
  - `review_text` (TextField): Текст отзыва.
  - `rating` (PositiveIntegerField, выбор с 1 по 10): Рейтинг, присвоенный пользователем.
  - `additional_comments` (TextField): Дополнительные комментарии или отзыв пользователя.
  - `created_at` (DateTimeField, автоматически создается): Временная метка создания отзыва.

```python
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField(default=datetime(1970, 1, 1))
    check_out_date = models.DateField(default=datetime(1970, 1, 1))
    review_text = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    additional_comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.hotel.name}'


```

### Профиль (Profile)

- Модель `Profile` представляет собой профиль пользователя с одним-к-одному отношением к модели User.

```python

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
```
