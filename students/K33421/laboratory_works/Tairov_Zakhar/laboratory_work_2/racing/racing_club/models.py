from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

class Racer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    full_name = models.TextField(null=True, verbose_name="Full name")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, verbose_name="Team")
    biography = models.TextField(null=True, verbose_name="Racer biography")
    num_of_races = models.IntegerField(verbose_name="Number of races", default=0)
    car_name = models.TextField(null=True, verbose_name="Car name")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Racer"
        verbose_name_plural = "Racers"

class Race(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Winner")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Race"
        verbose_name_plural = "Races"

class RaceEntry(models.Model):
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE, verbose_name="Racer")
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Race")

    class Meta:
        verbose_name = "Race participation"
        verbose_name_plural = "Race participations"

class Comment(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Race")
    poster = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Poster")
    text = models.TextField(verbose_name="Comment text")
    comment_type = models.CharField(
        max_length=32,
        choices= (
            ("suggests", "Suggestions"),
            ("races", "Races"),
            ("complaints", "Complaints"),
            ("other", "Misc")
        ),
        verbose_name="Comment type"
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Rating"
    )
    creation_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date and time posted")

    def __str__(self):
        return f"{self.poster.username} {self.comment_type}: {self.race.name}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"