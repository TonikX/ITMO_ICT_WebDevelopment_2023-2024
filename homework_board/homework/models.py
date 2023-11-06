from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField()
    deadline = models.DateField()
    task_text = models.TextField()
    penalty_info = models.TextField()

class Submission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    text_submission = models.TextField()

class Grade(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    grade = models.IntegerField()
    graded_by = models.ForeignKey(User, on_delete=models.CASCADE)
