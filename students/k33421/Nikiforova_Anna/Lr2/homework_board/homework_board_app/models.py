import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return self.name  # TODO: добавить информацию про учебный год в отображаемое название


class Student(AbstractUser):
    # username, email, password, password_confirmation
    fio = models.CharField(max_length=250)
    student_class = models.ForeignKey('Class', on_delete=models.CASCADE, null=True, default=None)
    submitted_homeworks = models.ManyToManyField('Homework', through='HomeworkSubmission')
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.fio


class Homework(models.Model):
    name = models.CharField(max_length=250)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    class_it_is_assigned_to = models.ForeignKey('Class', on_delete=models.CASCADE)
    date_of_issue = models.DateField(default=datetime.datetime.today())
    deadline_date = models.DateField()
    assignment_text = models.TextField()
    fines_information = models.TextField(blank=True, null=True)
    students_who_submitted_it = models.ManyToManyField('Student', through='HomeworkSubmission')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('homework_detail', args=[str(self.id)])

    def get_absolute_url_teacher(self):
        return reverse('teacher_homework_detail', args=[str(self.id)])

    def get_dates(self):
        return f"Выдано: {self.date_of_issue}, дедлайн: {self.deadline_date}"

    def snippet(self):
        return self.assignment_text[:250]


class HomeworkSubmission(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now_add=True)
    submission_text = models.TextField()
    grade = models.PositiveIntegerField(null=True, default=None)

    def get_absolute_url(self):
        return reverse('submitted_homework_detail', args=[str(self.id)])

    def snippet(self):
        return self.submission_text[:250]


class HomeworkDisplay:
    def __init__(self, homework, submission):
        self.homework = homework
        self.submission = submission

    def get_absolute_url(self):
        return self.homework.get_absolute_url()

    def snippet(self):
        return self.homework.snippet()

    def __str__(self):
        return self.homework.name

    def get_grade(self):
        return self.submission.grade if self.submission else None
