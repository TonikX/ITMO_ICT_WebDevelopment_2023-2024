from django.db import models
from django.contrib.auth import get_user_model


class Airplane(models.Model):
    name = models.CharField(max_length=30)
    seat_configuration = models.JSONField()
    

class Airline(models.Model):
    name = models.CharField(max_length=30)


class Flight(models.Model):
    DIRECTION_CHOICES = [
        ('arrival', 'Прилет'),
        ('departure', 'Вылет')
    ]
    STATUS_CHOICES = [
        ('scheduled', 'Запланирован'),
        ('cancelled', 'Отменен'),
        ('delayed', 'Опоздание'),
        ('boarding', 'На посадке'),
        ('in-flight', 'В пути'),
        ('landed', 'Приземлился'),
        ('completed', 'Завершен')
    ]
    
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='flights')
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flights')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    departure_location = models.CharField(max_length=30)
    arrival_location = models.CharField(max_length=30)
    direction = models.CharField(max_length=9, choices=DIRECTION_CHOICES)
    gate_number = models.CharField(max_length=6, null=True, blank=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='scheduled')


class Ticket(models.Model):
    SEAT_CLASS_CHOICES = [
        ('economy', 'Эконом'),
        ('comfort', 'Комфорт'),
        ('business', 'Бизнес'),
        ('first', 'Первый')
    ]

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tickets')
    seat_class = models.CharField(max_length=15, choices=SEAT_CLASS_CHOICES)
    seat = models.CharField(max_length=6)
    is_booked = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reservations')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='reservations')
    date_reserved = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reviews')
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
