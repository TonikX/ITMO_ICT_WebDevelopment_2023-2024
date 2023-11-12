from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)

class Conference(models.Model):
    title = models.CharField(max_length=200)
    topics = models.TextField()
    venue = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()

class Registration(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    conference = models.ForeignKey('Conference', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    approved_reg = models.BooleanField(default=False)

class Presentation(models.Model):
    conference = models.ForeignKey('Conference', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    approved_pres = models.BooleanField(default=False)

class Review(models.Model):
    conference = models.ForeignKey('Conference', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )