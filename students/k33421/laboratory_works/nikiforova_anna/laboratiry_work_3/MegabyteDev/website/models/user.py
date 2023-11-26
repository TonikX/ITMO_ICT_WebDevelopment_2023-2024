from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """ Расширение стандартной модели пользователя Django """
    patronymic = models.CharField(max_length=100, null=True, blank=True, verbose_name="Отчество")
    date_joined = models.DateField(null=False, default=timezone.now, verbose_name="Дата регистрации")
    profile_info = models.CharField(max_length=500, null=True, blank=True, verbose_name="Биография")
    profile_picture = models.ImageField(upload_to='images/users/', null=True,
                                        default='images/alt_image.jpg', verbose_name="Аватар")
    is_team_member = models.BooleanField(default=False, verbose_name="Член команды")
    full_name = models.CharField(max_length=255, blank=True,
                                 verbose_name="Полное имя")  # sort of caching for quick search
    article_participated = models.ManyToManyField('Article', through='Participant', related_name='parts',
                                                  verbose_name="Участники в создании")
    favourites = models.ManyToManyField('ContentObject', through='Favourite', related_name='favs',
                                        verbose_name="Избранное")

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'patronymic',
                        'profile_info', 'profile_picture']
    # TODO: create a possibility of logging in via social network

    def calculate_full_name(self):
        return f"{self.last_name} {self.first_name}{' ' + self.patronymic if self.patronymic else ''}"

    def save(self, *args, **kwargs):
        self.full_name = self.calculate_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
