from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.contenttypes.models import ContentType


class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    agency_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    birth_date = models.DateField(null=True)
    email = models.EmailField(unique=True, null=True)
    reserved_tours = models.ManyToManyField(Tour, through='Reservation')

    def __str__(self):
        return self.username


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # reservation_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    STATUS_CHOICES = [
        ('Ожидает подтверждения', 'Ожидает подтверждения'),
        ('Подтвержден', 'Подтвержден'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)


class TourComment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(choices=zip(range(1, 11), range(1, 11)))
    date_written = models.DateTimeField(auto_now_add=True)


