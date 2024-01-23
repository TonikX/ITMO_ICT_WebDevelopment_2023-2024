from django.contrib import admin
from .models import Teacher, Subject, Homework, Solution

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Homework)
admin.site.register(Solution)
