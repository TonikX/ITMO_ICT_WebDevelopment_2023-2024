from django.contrib import admin
from homeworks.models import User, Subject, Homework, HomeworkSubmission, HomeworkGrade
# Register your models here.

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Homework)
admin.site.register(HomeworkSubmission)
admin.site.register(HomeworkGrade)
