from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    description = models.TextField()
    team = models.CharField(max_length=100)
    rating = models.CharField(max_length=15,
                              choices=(('beginner', 'beginner'), ('middle', 'middle'), ('profy', 'profy')))
    car_num = models.CharField(max_length=30)
    car_description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Race(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Гонка'
        verbose_name_plural = 'Гонки'


class Register(models.Model):
    racer = models.ForeignKey(User, related_name='where_to_drive', on_delete=models.CASCADE)
    race = models.ForeignKey(Race, related_name='who_drive', on_delete=models.CASCADE)
    result = models.IntegerField(blank=True, null=True, )
    time_result = models.FloatField(blank=True, null=True, )

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'


class Comment(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, default="collaboration",
                            choices=(('collaboration', 'collaboration'),
                                     ('racing', 'racing'),
                                     ('other', 'other')))
    message = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
