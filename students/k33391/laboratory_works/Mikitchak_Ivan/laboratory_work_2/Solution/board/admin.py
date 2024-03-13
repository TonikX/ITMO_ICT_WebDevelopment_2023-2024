from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(Subject)
admin.site.register(Educator)
admin.site.register(Student)
admin.site.register(Homework)
admin.site.register(Solution)
admin.site.register(Grade)
