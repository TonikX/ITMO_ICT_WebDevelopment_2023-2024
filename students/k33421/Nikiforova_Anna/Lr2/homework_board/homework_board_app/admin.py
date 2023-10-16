from django.contrib import admin
from .models import Subject, Class, Homework, Student, HomeworkSubmission


for model in [Subject, Class, Homework, Student, HomeworkSubmission]:
    admin.site.register(model)
