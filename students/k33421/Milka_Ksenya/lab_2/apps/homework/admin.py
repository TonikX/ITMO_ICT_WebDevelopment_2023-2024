from django.contrib import admin

from apps.homework.models import Subject, SubjectTeacher, Homework, Submission, Grade

admin.site.register(Subject)
admin.site.register(SubjectTeacher)
admin.site.register(Homework)
admin.site.register(Submission)
admin.site.register(Grade)
