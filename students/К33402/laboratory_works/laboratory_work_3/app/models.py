from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Lesson(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LessonTeacher(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='who_teach', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='what_teach', on_delete=models.CASCADE)


class StudentClass(models.Model):
    letter = models.CharField(max_length=2)
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])

    def __str__(self):
        return f"{self.year}{self.letter}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=2, choices=(
        ('f', 'f'),
        ('m', 'm')
    ))
    student_class = models.ForeignKey(StudentClass, related_name='students_in_class', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    num = models.CharField(max_length=4)
    base = models.BooleanField(default=True)

    def __str__(self):
        return self.num


class Schedule(models.Model):
    day = models.CharField(max_length=10, choices=(
        ('пн', 'пн'),
        ('вт', 'вт'),
        ('ср', 'ср'),
        ('чт', 'чт'),
        ('пт', 'пт'),
        ('сб', 'сб'),
        ('вс', 'вс'),
    ))

    num_lesson = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])

    student_class = models.ForeignKey(StudentClass, related_name='sc_schedule', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='room_schedule', on_delete=models.CASCADE)
    lesson_teacher = models.ForeignKey(LessonTeacher, related_name='lt_schedule', on_delete=models.CASCADE)


class Mark(models.Model):

    student = models.ForeignKey(Student, related_name='student_marks', on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, related_name='all_marks', on_delete=models.CASCADE)

    mark = models.IntegerField(validators=[MinValueValidator(1),MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.mark

