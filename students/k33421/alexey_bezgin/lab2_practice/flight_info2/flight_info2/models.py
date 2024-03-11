from django.contrib.auth.models import User
from django.core import validators
from django.db import models


class Airline(models.Model):
    class Meta:
        verbose_name = 'Авиакомпания'
        verbose_name_plural = "Авиакомпании"

    name = models.CharField(max_length=50, verbose_name="Название")

    def __str__(self):
        return f"{self.name}"


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
