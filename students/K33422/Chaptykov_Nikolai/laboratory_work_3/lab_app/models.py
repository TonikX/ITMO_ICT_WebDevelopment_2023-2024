from django.db import models


DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class Tutor(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"


class AcademicGroup(models.Model):
    group_name = models.CharField(max_length=30)
    faculty = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.group_name}, {self.faculty}"


class Student(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname} {self.group}"


"""
    Discipline хранит название дисциплины, преподавателя и закрепленный
    за ним кабинет. Учитывать проведение лекций и практик в разных 
    аудиториях можно с помощью введения поля для маркера, также можно 
    добавлять уточняющий префикс к названию дисциплины: 'Вышмат лекция'
    и 'Вышмат практика'
"""
class Discipline(models.Model):
    lecturer = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    discipline_name = models.CharField(max_length=30)
    room = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"каб. {self.room}, {self.discipline_name}, ведет {self.lecturer}"


"""
    По одному предмету может быть несколько занятий в разное время,
    введем сущность Lecture чтобы не дублировать данные дисциплин
"""
class Lecture(models.Model):
    discipline = models.ForeignKey(Discipline, related_name='lecture', on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS_OF_WEEK, default=0)
    time = models.TimeField(null=True)

    def __str__(self):
        return f"{DAYS_OF_WEEK[self.day][1]} {self.discipline}"


"""
    На одном занятии может находится несколько групп, введем
    ассоциативную сущность между лекцией и группой чтобы это учитывать
"""
class AssignedLecture(models.Model):
    group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE, primary_key=True)
    lecture = models.ManyToManyField(Lecture)

    def __str__(self):
        return f"{self.group}" + f"{self.lecture}"


class AcademicPerformance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)


