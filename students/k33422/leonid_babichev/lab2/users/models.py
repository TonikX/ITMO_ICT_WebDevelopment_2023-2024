from django.contrib.auth.models import AbstractUser
from django.db import models


class Tourist(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport = models.CharField(max_length=10)
