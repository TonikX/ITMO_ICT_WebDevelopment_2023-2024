from django.contrib.auth.models import User
from django.db import models


class RacerCar(models.Model):
    state_number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=30, null=False)
    model = models.CharField(max_length=30, null=False)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.state_number} {self.brand} {self.model}"


class Racer(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    team_name = models.CharField(max_length=100, null=False)
    participant_description = models.TextField(max_length=500, default='Нет описания')
    experience = models.PositiveIntegerField(null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    car = models.OneToOneField(RacerCar, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.team_name}"


class Race(models.Model):
    title = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(null=False)
    location = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, default='Нет описания')

    def __str__(self):
        return f"Гонка: {self.title}, {self.date}"


class RaceResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=False)
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE, null=False)
    position = models.PositiveIntegerField(null=False)
    lap_time = models.DurationField(null=False)
    top_speed = models.FloatField(null=False)

    def __str__(self):
        return f"Результат для {self.racer.last_name} в гонке {self.race.title}, {self.race.date}"


class Registration(models.Model):
    racer = models.ForeignKey(Racer, on_delete=models.DO_NOTHING, null=False)
    race = models.ForeignKey(Race, on_delete=models.DO_NOTHING, null=False)
    registration_date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f"{self.race.title}"


class Comment(models.Model):
    COMMENT_TYPES = (
        ('Cooperation', 'Question about cooperation'),
        ('Race', 'Question about the race'),
        ('Other', 'Other'),
    )

    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=False)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    comment_date = models.DateTimeField(auto_now_add=True, null=False)
    comment_text = models.TextField(null=False)
    comment_type = models.CharField(max_length=20, choices=COMMENT_TYPES, null=False)
    rating = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"Комментарий от {self.commentator.username} для {self.race.location}"
