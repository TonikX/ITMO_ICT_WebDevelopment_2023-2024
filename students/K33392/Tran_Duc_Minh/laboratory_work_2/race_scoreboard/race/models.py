from django.core.validators import MaxValueValidator
from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Race(models.Model):
    race_name = models.CharField(max_length=100)
    race_date = models.DateField()
    registration_deadline = models.DateField()

    def __str__(self):
        return self.race_name

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    car_description = models.TextField()
    experience = models.IntegerField()
    registered_races = models.ManyToManyField(Race, through='RaceRegistration')

    def __str__(self):
        return f'{self.user.username} ({self.team.name})'

class RaceRegistration(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)

class RaceResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    race_time = models.DurationField()  # Thời gian thực hiện trong cuộc đua
    finishing_position = models.PositiveIntegerField()  # Vị trí kết thúc cuộc đua

    def __str__(self):
        return f'{self.participant.user.username} in {self.race.race_name}'

class Commentator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Comment(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    commentator = models.ForeignKey(Commentator, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField()
    COMMENT_TYPE_CHOICES = [
        ('Cooperation', 'Questions about cooperation'),
        ('Racing', 'Questions about racing'),
        ('Other', 'Other'),
    ]
    comment_type = models.CharField(
        max_length=100,
        choices=COMMENT_TYPE_CHOICES,
        default='Other'
    )
    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(10)]
    )
