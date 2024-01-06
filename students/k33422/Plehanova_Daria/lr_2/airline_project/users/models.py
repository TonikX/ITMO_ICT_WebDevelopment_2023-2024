from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    email = models.EmailField(blank=True, null=True, verbose_name='Адрес почты')
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='Номер телефона')
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Отчество')
    citizenship = models.CharField(max_length=100, blank=True, null=True, verbose_name='Гражданство')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True, verbose_name='Пол')
