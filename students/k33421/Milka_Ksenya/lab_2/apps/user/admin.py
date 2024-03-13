from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.user.models import Student, Teacher

User = get_user_model()

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(User)
