from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class Tourist(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport = models.CharField(max_length=10)
