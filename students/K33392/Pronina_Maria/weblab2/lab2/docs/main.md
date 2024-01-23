# Задание

### Вариант2:
###Доска домашних заданий.<br>
О домашнем задании должна храниться следующая информация: предмет,
преподаватель, дата выдачи, период выполнения, текст задания, информация о штрафах.<br>
Необходимо реализовать следующий функционал:<br>
Регистрация новых пользователей.<br>
Просмотр домашних заданий по всем дисциплинам (сроки выполнения,
описание задания).<br>
Сдача домашних заданий в текстовом виде.<br>
Администратор (учитель) должен иметь возможность поставить оценку за
задание средствами Django-admin.<br>
В клиентской части должна формироваться таблица, отображающая оценки
всех учеников класса.<br>

Были написаны следующие модели:
```python
# хранит и учителей и учеников, которые разделены по группам, у учителей есть уникальные права
class Teacher(AbstractUser):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Subject(models.Model): #предметы
    name = models.CharField(max_length=100)


class Homework(models.Model):
    teacher = models.ForeignKey(User, limit_choices_to={'groups__name': "Teachers"}, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    release_date = models.DateTimeField(default=datetime.datetime.now())
    deadline = models.DateTimeField()
    description = models.CharField(max_length=1000)
    penalty = models.CharField(max_length=1000, default=None, blank=True, null=True)


class Solution(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'groups__name': "Students"}, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution_text = models.CharField(max_length=1000)
    status = [
        ('CHECK', 'Checked'),
        ('WAIT', 'Waiting to be checked')
    ]
    mark = models.IntegerField(default=None, blank=True, null=True)

```

Адресация:
```python
from django.urls import path
from . import views


urlpatterns = [
    path('teacher/new', views.teacher_form_view),
    path('teacher/success', views.teacher_add_success_view),
    path('student/new', views.student_form_view),
    path('student/success', views.student_add_success_view),
    path('homeworks', views.homeworks_view),
    path('homeworks/new/<hw_id>', views.solution_form_view),
    path('solution/success', views.solution_add_success_view),
    path('register', views.register_view),
]
```