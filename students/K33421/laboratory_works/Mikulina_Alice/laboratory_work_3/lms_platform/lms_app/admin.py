from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Application)
admin.site.register(Completion)