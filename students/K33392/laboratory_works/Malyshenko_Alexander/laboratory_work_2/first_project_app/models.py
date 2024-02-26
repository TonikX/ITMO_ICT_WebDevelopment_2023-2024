import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class User(AbstractUser):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True)
    is_racer = models.BooleanField(default=False)


class Racer(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)
    experience = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    drive_class = models.CharField(max_length=50)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(max_length=100)
    car_description = models.CharField(max_length=100, blank=True)


class Race(models.Model):
    nt, p, o, ps = "not started", "in progress", "over", "pause"
    status_types = {
        nt: "The race has not started yet",
        p: "The race is in progress",
        o: "The race is over",
        ps: "The race is suspended"
    }

    race_location = models.CharField(max_length=50)
    winner_id = models.ForeignKey(Racer, on_delete=models.CASCADE, blank=True, null=True)
    winner_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    users_id = models.ManyToManyField("Racer", through="Statistic", related_name="users_id")
    race_date = models.DateField(default=datetime.datetime.today())
    status = models.CharField(max_length=20, choices=status_types, default=nt)


class Statistic(models.Model):
    user_id = models.ForeignKey(Racer, on_delete=models.CASCADE)
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE)
    loop = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, null=True)
    time = models.TimeField(blank=True, null=True)


class Comment(models.Model):
    c, r, o = "collab", "race", "other"
    comment_types = {
        c: "questions about collaboration",
        r: "questions about race",
        o: "other questions"
    }

    main_text = models.TextField(max_length=3000, blank=True)
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE)
    race_date = models.DateField()
    type = models.CharField(choices=comment_types, default=o, max_length=20)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    commentator_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
