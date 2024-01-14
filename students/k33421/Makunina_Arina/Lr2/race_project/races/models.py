from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"


class Racer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, verbose_name="Команда")
    description = models.TextField(verbose_name="Описание")
    experience = models.IntegerField(verbose_name="Опыт")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Гонщик"
        verbose_name_plural = "Гонщики"


class Race(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Победитель")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Гонка"
        verbose_name_plural = "Гонки"


class RaceResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Гонка")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Команда")
    time_taken = models.DurationField(verbose_name="Время прохождения")

    def __str__(self):
        return f"{self.race.name} - {self.team.name} - {self.time_taken}"

    class Meta:
        verbose_name = "Результат гонки"
        verbose_name_plural = "Результаты гонок"


class RaceEntry(models.Model):
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE, verbose_name="Гонщик")
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Гонка")

    class Meta:
        verbose_name = "Участие в гонке"
        verbose_name_plural = "Участия в гонках"


class Comment(models.Model):
    COMMENT_TYPES = (
        ("cooperation", "Предложения"),
        ("race", "Гонки"),
        ("complaint", "Жалоба"),
        ("other", "Другое"),
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Гонка")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст комментария")
    comment_type = models.CharField(
        max_length=20,
        choices=COMMENT_TYPES,
        verbose_name="Тип комментария"
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.author.username} - {self.comment_type} - {self.race.name}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
