from django.contrib import admin
from .models import Homework, Profile, SubmittedHomework, GradeJournal, Subject

admin.site.register(Homework)
admin.site.register(Profile)
admin.site.register(SubmittedHomework)
admin.site.register(GradeJournal)
admin.site.register(Subject)