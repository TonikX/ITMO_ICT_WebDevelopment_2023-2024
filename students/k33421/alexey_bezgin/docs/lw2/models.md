# Схема данных

### 1. Авиакомпания

Мы храним информацию о существующих авиакомпаниях. В моем случае я храню только информацию о названии, но атрибуты можно расширить.

```python
class Airline(models.Model):
    class Meta:
        verbose_name = 'Авиакомпания'
        verbose_name_plural = "Авиакомпании"

    name = models.CharField(max_length=50, verbose_name="Название")

    def __str__(self):
        return f"{self.name}"
```
### 2. Рейс

Мы храним информацию о рейсе: авиакомпании, его типе (отлет или прилет), гейте, времени отправления и прибытия.

```python
class Flight(models.Model):
    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = "Рейсы"

    class Type(models.TextChoices):
        DEPARTURE = "departure", "Отлёт"
        ARRIVAL = "arrival", "Прилёт"

    def __str__(self):
        return f"Flight {self.id}"

    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name="flights", verbose_name="Авиакомпания")
    type = models.CharField(max_length=9, choices=Type.choices, verbose_name="Тип")
    gate = models.CharField(max_length=5, verbose_name="Гейт")
    departure = models.DateTimeField(verbose_name="Время отправления")
    arrival = models.DateTimeField(verbose_name="Время прибытия")
```


### 3. Бронирование

Мы храним информацию о клиенте, сделавшем бронь, рейсе, подтверждении регистрации, номере билета и номере кресла (в данной реализации без номера ряда и сидения).

```python 
class Reservation(models.Model):
    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = "Бронирования"

    def __str__(self):
        return f"Reservation {self.id}"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Reservations", verbose_name="Пассажир")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="Reservations", verbose_name="Рейс")
    registered = models.BooleanField(default=False, verbose_name="Подтверждение регистрации")
    ticket = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Номер билета")
    seat = models.CharField(max_length=2, choices=[tuple([str(ind), str(ind)]) for ind in range(1, 11)], unique=True)
```


### 4. Отзыв

Создадим отдельную модель для создания отзывов о рейсах. Будем хранить информацию об авторе, рейсе, дату, текст отзыва и рейтинг от 1 до 10. 

```python
class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Review {self.id}"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks", verbose_name="Пассажир")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="feedbacks", verbose_name="Рейс")
    text = models.TextField(verbose_name="Текст")
    rating = models.PositiveSmallIntegerField(
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(10)], verbose_name="Рейтинг"
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
```
