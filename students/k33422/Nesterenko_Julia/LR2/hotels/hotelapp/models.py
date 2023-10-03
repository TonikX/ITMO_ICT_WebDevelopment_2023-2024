import datetime
import os
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from .manager import GuestManager


class Guest(AbstractUser):
    country = models.CharField(max_length=30)
    photo = models.ImageField(blank=True, default='user.svg')

    REQUIRED_FIELDS = []
    objects = GuestManager()

    @property
    def bookings(self):
        return Booking.objects.filter(guest=self)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    description = models.TextField(blank=True, null=True)

    @property
    def rooms(self):
        return Room.objects.filter(hotel=self)

    @property
    def guests(self):
        guestlist = []
        for room in self.rooms:
            guestlist.extend(room.get_last_month_guests())
        return list(set(guestlist))


class Room(models.Model):
    type_CH = ('Apartment', 'Dormitory', 'Standard', 'Suite', 'Deluxe', 'Superior')
    type = models.CharField(choices=zip(type_CH, type_CH), max_length=10)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    capacity = models.PositiveSmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(10)))
    thumbnail = models.ImageField()
    comm_CH = ('Bathroom', 'Swimming pool', 'Parking',
               'Wi-Fi', 'Air conditioner', 'Room service',
               'Breakfast', 'Balcony', 'Refrigerator')
    commodities = MultiSelectField(choices=zip(comm_CH, comm_CH), max_choices=9, max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0)])

    @property
    def reviews(self):
        bookings = Booking.objects.filter(room=self)
        return Review.objects.filter(booking__in=bookings)

    def available(self, start, end):
        start = datetime.date.fromisoformat(start)
        end = datetime.date.fromisoformat(end)
        bookings = (Booking.objects.filter(room=self, status='Active') |
                    Booking.objects.filter(room=self, status='Awaits'))
        for book in bookings:
            if ((start <= book.date_from and end >= book.date_until) or
                    (book.date_from <= start <= book.date_until) or
                    (book.date_from <= end <= book.date_until)):
                return False
        return True

    def get_last_month_guests(self):
        today = datetime.date.today()
        month_before = today - datetime.timedelta(days=30)
        bookings = Booking.objects.filter(room=self, date_until__range=[month_before, today])
        return [b.guest for b in bookings]


class Booking(models.Model):
    guest = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status_CH = ('Active', 'Awaits', 'Finished', 'Canceled')
    status = models.CharField(choices=zip(status_CH, status_CH), max_length=10)
    date_from = models.DateField()
    date_until = models.DateField()

    @property
    def total_price(self):
        days = (self.date_until - self.date_from).days
        days = days if days != 0 else 1
        return self.room.price * days


class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    rating_CH = ('1', '2', '3', '4', '5')
    rating = models.CharField(choices=zip(rating_CH, rating_CH), max_length=1)
    body = models.TextField()
