from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (CASCADE, BooleanField, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
                              ManyToManyField, Model, TextField)


class Traveler(AbstractUser):
    reservations = ManyToManyField("Reservation")


class Tour(Model):
    name = CharField(max_length=200)
    description = TextField(null=True)
    start_date = DateField()
    end_date = DateField()
    country = ForeignKey("Country")
    travelers = ManyToManyField(Traveler)
    payment_details = TextField()
    tour_agency = ForeignKey("TourAgency", CASCADE)


class Reservation(Model):
    traveler = ForeignKey(Traveler, CASCADE)
    tour = ForeignKey(Tour, CASCADE)
    reserved_at = DateTimeField(auto_now_add=True)
    confirmed = BooleanField(default=False)


class Review(Model):
    tour = ForeignKey(Tour, CASCADE)
    traveler = ForeignKey(Traveler, CASCADE)
    review_datetime = DateTimeField(auto_now_add=True)
    comment = TextField()
    rating = IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


class TourAgency(Model):
    name = CharField(max_length=50)
    tours = ManyToManyField(Tour)


class Country(Model):
    code = CharField(max_length=3)  # iso 3166
    display_name = CharField(max_length=50)
    tours = ManyToManyField(Tour)
