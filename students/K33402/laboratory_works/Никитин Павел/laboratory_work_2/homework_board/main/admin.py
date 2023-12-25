from django.contrib import admin
from .models import User, SubmittedWork, Homework


admin.site.register(User)
admin.site.register(Homework)
admin.site.register(SubmittedWork)