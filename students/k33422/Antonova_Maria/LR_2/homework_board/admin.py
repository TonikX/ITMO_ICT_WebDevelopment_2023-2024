from django.contrib import admin
from .models import Homework, Answer, JournalRecord


class HomeworkAdmin(admin.ModelAdmin):  # наследует функциональность класса, для отображения homework в adminе
    list_display = ('title', 'subject', 'teacher',
                    'due_date')  # указывает  список полей модели Homework, которые будут отображаться в списке объектов


class AnswerAdmin(admin.ModelAdmin):  # наследует функциональность класса, для отображения answers в adminе
    list_display = (
    '__str__', 'date_created')  # указывает  список полей модели, которые будут отображаться в списке объектов


@admin.register(JournalRecord)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('homework', 'student', 'grade')


admin.site.register(Homework, HomeworkAdmin)  # для управления через интерф админа
admin.site.register(Answer, AnswerAdmin)
