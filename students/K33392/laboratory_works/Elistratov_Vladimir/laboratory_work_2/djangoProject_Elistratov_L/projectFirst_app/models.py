from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

from django.conf import settings
# Create your models here.


class Tour(models.Model):
    name = models.CharField(max_length=20)
    target = models.CharField(max_length=40)
    duration = models.IntegerField()
    tourTypes = [
        ("AllIn", "All inclusive"),
        ("T&A", "Travel and accommodation"),
    ]
    type = models.CharField(max_length=30, choices=tourTypes)
    cost = models.IntegerField()
    description = models.TextField(max_length=1000)


class Person(AbstractUser):
    fullName = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    pSeries = models.CharField(max_length=4, blank=True)
    pNumber = models.CharField(max_length=6, blank=True)
    bookedTours = models.ManyToManyField(Tour, through='Treaty')


class Treaty(models.Model):
    customerID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tourID = models.ForeignKey(Tour, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    statusVariation = [
        ("w", "awaiting confirmation"),
        ("a", "approved"),
        ("r", "rejected"),
        ("e", "ended")
    ]
    status = models.CharField(max_length=50, choices=statusVariation)
    pNum = models.IntegerField()
    cost = models.IntegerField()


class Comments(models.Model):
    authorID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tourID = models.ForeignKey(Tour, on_delete=models.CASCADE)
    tStartDate = models.DateField()
    tEndDate = models.DateField()
    commentText = models.TextField(max_length=1000, blank=True)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

