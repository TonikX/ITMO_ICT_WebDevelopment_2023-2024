from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    # Многие ко многим для связи с задачами через TaskUserRelation
    related_tasks = models.ManyToManyField('Task', through='TaskUserRelation', related_name='users')


class TaskUserRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    completed_choices = [
        ('в работе', 'В работе'),
        ('запланирована', 'Запланирована'),
        ('завершена', 'Завершена'),
    ]
    completed = models.CharField(max_length=20, choices=completed_choices)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    aim = models.ForeignKey('Aim', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Aim(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    status_choices = [
        ('выполнена', 'Выполнена'),
        ('не выполнена', 'Не выполнена'),
    ]
    status = models.CharField(max_length=20, choices=status_choices)


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_user_relation = models.ForeignKey(TaskUserRelation, on_delete=models.CASCADE)

