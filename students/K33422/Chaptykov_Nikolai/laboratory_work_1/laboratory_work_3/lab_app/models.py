from django.db import models


class Tutor(models.Model):
	surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group(models.Model):
	group_name = models.CharField(max_length=30)
	faculty = models.CharField(max_length=30)

	def __str__(self):
        return f"{self.group_name}, {self.faculty}"


class Student(models.Model):
	surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}, {self.group}"


"""
	На одном занятии может находится несколько групп, введем
	ассоциативную сущность между лекцией и группой чтобы это учитывать
"""
class AssignedLecture(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, primary_key=True)
    lecture = models.ForeignKey(Lecture)


"""
	Discipline хранит название дисциплины, преподавателя и закрепленный
	за ним кабинет. Учитывать проведение лекций и практик в разных 
	аудиториях можно с помощью введения поля для маркера, также можно 
	добавлять уточняющий префикс к названию дисциплины: 'Вышмат лекция'
	и 'Вышмат практика'
"""
class Discipline(models.Model):
	lecturer = models.ForeignKey(Tutor, on_delete=mmodels.CASCADE)
	discipline_name = models.CharField(max_length=30)
	room = models.CharField(max_length=30, blank=True)

	def __str__(self):
        return f"{self.room}, {self.discipline_name}\n{self.lecturer}"


"""
	По одному предмету может быть несколько занятий в разное время,
	введем сущность Lecture чтобы не дублировать данные дисциплин
"""
class Lecture(models.Model):
	discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
	time = models.DateField()

	def __str__(self):
        return f"{self.time}\n{self.discipline}"


class AcademicPerformance(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.ForeignKey(Discipline, on_delete=models.CASCADE)
	grade = models.CharField(max_length=10)


