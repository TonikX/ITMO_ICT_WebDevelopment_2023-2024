from django.db import models
from django.contrib.auth.models import User


class Homework(models.Model):
    title = models.CharField(max_length=100)  # ля хранения информации о названии, предмете и учителе по дз
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    description = models.TextField()  # + для хранения описания домашнего задания и информации о штрафах
    due_date = models.DateTimeField()
    penalty_info = models.TextField()

    def __str__(self):
        return self.title  # названеи будет использоваться для представления объектов модели Homework


class Answer(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE,
                                 related_name='answers')  # связь с домашним заданием
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')  # внешний ключ  на  User
    answer_text = models.TextField()  # ля хранения текста ответа
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.homework} - {self.student.last_name} {self.student.first_name[0]}.'
        # название домашнего задания, фамилию и имя пользователя (1-я буква), будет использоваться для представления объектов модели Answer


class JournalRecord(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='journals')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journals')
    grade = models.IntegerField(null=True)


