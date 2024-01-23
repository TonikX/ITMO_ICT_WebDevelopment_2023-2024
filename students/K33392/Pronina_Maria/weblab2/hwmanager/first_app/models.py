import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Teacher(AbstractUser):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


User = get_user_model()


class Subject(models.Model):
    name = models.CharField(max_length=100)


class Homework(models.Model):
    teacher = models.ForeignKey(User, limit_choices_to={'groups__name': "Teachers"}, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    release_date = models.DateTimeField(default=datetime.datetime.now())
    deadline = models.DateTimeField()
    description = models.CharField(max_length=1000)
    penalty = models.CharField(max_length=1000, default=None, blank=True, null=True)


class Solution(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'groups__name': "Students"}, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution_text = models.CharField(max_length=1000)
    status = [
        ('CHECK', 'Checked'),
        ('WAIT', 'Waiting to be checked')
    ]
    mark = models.IntegerField(default=None, blank=True, null=True)
