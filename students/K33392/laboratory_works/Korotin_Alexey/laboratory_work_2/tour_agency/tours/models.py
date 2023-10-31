from django.db import models
from users.models import Tourist


class Tour(models.Model):
    name = models.CharField(max_length=300)
    destination = models.CharField(max_length=200)
    tourists = models.ManyToManyField(Tourist, through='Reservation')


class Reservation(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.DO_NOTHING)
    tour = models.ForeignKey(Tour, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)


class Review(models.Model):
    rating = models.IntegerField()
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=1000)
