from django.contrib import admin
from .models import *


admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(LessonTeacher)
admin.site.register(Student)
admin.site.register(StudentClass)
admin.site.register(Schedule)
admin.site.register(Mark)
