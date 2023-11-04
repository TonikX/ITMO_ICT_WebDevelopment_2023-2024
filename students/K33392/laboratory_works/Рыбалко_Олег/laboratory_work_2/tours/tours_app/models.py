from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (CASCADE, BooleanField, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
                              ManyToManyField, Model, TextField)


class Traveler(AbstractUser):
    pass


class Tour(Model):
    name = CharField(max_length=200)
    description = TextField(null=True)
    country = ForeignKey("Country", CASCADE)
    payment_details = TextField()
    tour_agency = ForeignKey("TourAgency", CASCADE)

    def __str__(self) -> str:
        return self.name


class TourDate(Model):
    tour = ForeignKey(Tour, CASCADE)
    start_date = DateField()
    end_date = DateField()


class Reservation(Model):
    traveler = ForeignKey(Traveler, CASCADE)
    tour_date = ForeignKey(TourDate, CASCADE)
    reserved_at = DateTimeField(auto_now_add=True)
    confirmed = BooleanField(default=False)


class Review(Model):
    tour_date = ForeignKey(TourDate, CASCADE)
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
