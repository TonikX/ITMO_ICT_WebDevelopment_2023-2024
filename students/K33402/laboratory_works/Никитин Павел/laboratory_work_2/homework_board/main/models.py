from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    def __str__(self):
      return self.username


class Homework(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField()
    deadline = models.DateTimeField()

class SubmittedWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    text = models.TextField()
    STATUS_CHOICES = [
        ('pending', 'Ожидает проверки'),
        ('checked', 'Проверено'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    grade = models.IntegerField(null=True, blank=True)
