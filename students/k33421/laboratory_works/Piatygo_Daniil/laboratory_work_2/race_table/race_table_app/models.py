from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Racer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    experience = models.IntegerField()


class Race(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)


class RaceEntry(models.Model):
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Comment(models.Model):
    COMMENT_TYPES = (
        ("cooperation", "Вопрос о сотрудничестве"),
        ("race", "Вопрос о гонках"),
        ("other", "Иное"),
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment_type = models.CharField(max_length=20, choices=COMMENT_TYPES)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
