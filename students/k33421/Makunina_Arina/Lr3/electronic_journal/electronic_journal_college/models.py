from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Room {self.number}"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    course = models.PositiveSmallIntegerField(validators=[MaxValueValidator(4)])

    def __str__(self):
        return f"{self.name} ({self.course} курс)"


class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, related_name="students", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    class DayOfWeek(models.TextChoices):
        MONDAY = "monday", "Понедельник"
        TUESDAY = "tuesday", "Вторник"
        WEDNESDAY = "wednesday", "Среда"
        THURSDAY = "thursday", "Четверг"
        FRIDAY = "friday", "Пятница"
        SATURDAY = "saturday", "Суббота"
        SUNDAY = "sunday", "Воскресенье"

    day_of_week = models.CharField(max_length=9, choices=DayOfWeek.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        day_display = self.get_day_of_week_display()
        start_time_str = self.start_time.strftime('%H:%M')
        end_time_str = self.end_time.strftime('%H:%M')
        return f"{day_display} {start_time_str} - {end_time_str}"


class Schedule(models.Model):
    group = models.ForeignKey(Group, related_name="schedules", on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(validators=[MaxValueValidator(8)])
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name="schedules", on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"{self.group.name} {self.timeslot.get_day_of_week_display()} {self.timeslot.start_time} - "
            f"{self.timeslot.end_time}, Room: {self.room.number} - {self.discipline.name} by {self.teacher.name}"
        )


class Grade(models.Model):
    semester = models.PositiveSmallIntegerField(validators=[MaxValueValidator(8)])
    discipline = models.ForeignKey(Discipline, related_name="grades", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="grades", on_delete=models.CASCADE)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ("semester", "discipline", "student")

    def __str__(self):
        return f"{self.student.name} - {self.discipline.name} - Grade: {self.grade}"


class UserRole(models.Model):
    class Role(models.TextChoices):
        SUB_DEAN = "sub_dean", "Заместитель декана"
        DISPATCHER = "dispatcher", "Диспетчер"

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="role", verbose_name="Пользователь")
    role = models.CharField(max_length=10, choices=Role.choices, verbose_name="Роль")

    def __str__(self):
        return self.role