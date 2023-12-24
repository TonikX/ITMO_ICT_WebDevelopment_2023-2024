from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Traveler(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    passport = models.CharField(max_length=30)
    flights = models.ManyToManyField('Flight', through='Ticket')
    seats = models.ManyToManyField('Seat', through='Ticket')


class Ticket(models.Model):
    traveler_id = models.ForeignKey('Traveler', on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)
    seat_id = models.ForeignKey('Seat', on_delete=models.CASCADE)
    baggage = models.BooleanField(default=False)


class Flight(models.Model):
    airline = models.CharField(max_length=30)
    departure_site = models.CharField(max_length=50)
    landing_site = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    landing_time = models.DateTimeField()
    gate = models.CharField(max_length=10)
    plane_id = models.ForeignKey('Plane', on_delete=models.CASCADE)
    travelers = models.ManyToManyField('Traveler', through='Ticket')
    seats = models.ManyToManyField('Seat', through='Ticket')

    def __str__(self):
        return self.departure_site + '-' + self.landing_site# + '(' + self.departure_time + '-' + self.landing_time + ')'


class Seat(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    category = models.CharField(max_length=20)
    cost = models.IntegerField()
    plane_id = models.ForeignKey('Plane', on_delete=models.CASCADE)
    flights = models.ManyToManyField('Flight', through='Ticket')
    travelers = models.ManyToManyField('Traveler', through='Ticket')

    def __str__(self):
        return self.name


class Plane(models.Model):
    name = models.CharField(max_length=50)
    seats_number = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    flight = models.ForeignKey('Flight', related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey('Traveler', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(
         validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_flight = models.DateTimeField()

