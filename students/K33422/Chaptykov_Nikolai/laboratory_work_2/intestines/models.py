from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime
from django.shortcuts import get_object_or_404


class SchoolGroup(models.Model):
    grade = models.CharField(max_length=2, default='0')
    letter_id = models.CharField(max_length=1, default='Ъ')

    def __str__(self):
        return f"{self.grade}{self.letter_id}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    group = models.ForeignKey(SchoolGroup, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Discipline(models.Model):
    discipline = models.CharField(max_length=30)

    def __str__(self):
        return self.discipline


class Homework(models.Model):
    discipline_object = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    teacher_object = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    schoolgroup_object = models.ForeignKey(SchoolGroup, on_delete=models.CASCADE, default=0)
    date_received = models.DateField()
    date_deadline = models.DateField()
    task = models.CharField(max_length=200)
    penalty = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.discipline_object} {self.schoolgroup_object}"


class AssignedHomework(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    work_object = models.ForeignKey(Homework, on_delete=models.CASCADE)
    datetime.datetime.now()
    task = models.CharField(max_length=200)


class StudentGrade(models.Model):
    homework_object = models.ForeignKey(AssignedHomework, on_delete=models.CASCADE)
    grade = models.CharField(max_length=1)

    def save(self, *args, **kwargs):
        super(StudentGrade, self).save(*args, **kwargs)
        ahw = get_object_or_404(AssignedHomework, id=self.homework_object.id)
        student = get_object_or_404(Student, user=ahw.user)
        try:
            performance_object = StudentPerformance.objects.get(student_object=student, discipline_object=ahw.work_object.discipline_object)
            performance_object.grades.add(self)
        except StudentPerformance.DoesNotExist:
            temp = StudentPerformance.objects.create(student_object=student, discipline_object=ahw.work_object.discipline_object)
            temp.grades.add(self)

    def __str__(self):
        return f"{self.grade}"


class StudentPerformance(models.Model):
    student_object = models.ForeignKey(Student, on_delete=models.CASCADE)
    discipline_object = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    grades = models.ManyToManyField(StudentGrade)


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
