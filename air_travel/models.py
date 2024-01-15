from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'user'


class Flight(models.Model):
    company_name = models.CharField(max_length=30, null=False, blank=False)
    gate = models.CharField(max_length=30, blank=False)
    plane_number = models.CharField(max_length=30, blank=False)
    date_arrivals = models.DateTimeField(blank=True, null=True)
    date_departures = models.DateTimeField(blank=True, null=True)
    seat_place = models.IntegerField()

    def __str__(self):
        return f'{self.id}' # возвращаем номер рейса


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.flight.id}'


class Comments(models.Model):
    text = models.CharField(max_length=500, null=True, blank=True)
    rate = models.IntegerField(null=False, blank=False)
    booking = models.ForeignKey(Booking, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.text}'
