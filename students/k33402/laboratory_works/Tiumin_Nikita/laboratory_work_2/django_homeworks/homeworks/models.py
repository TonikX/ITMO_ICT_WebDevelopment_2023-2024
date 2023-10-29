from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    issue_date = models.DateField()
    deadline = models.DateField()
    description = models.TextField()
    penalties = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"Домашнее задание по {self.subject.name}"


class HomeworkSubmission(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    submission_text = models.TextField()
    submission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Сдача задания '{self.homework}' от {self.student.username}"


class HomeworkGrade(models.Model):
    homework_submission = models.OneToOneField(HomeworkSubmission, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField()
    graded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    graded_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Оценка за сдачу '{self.homework_submission.homework}' от {self.homework_submission.student.username}"
