from django.contrib import admin
from .models import *


class Admin(admin.ModelAdmin):
    admin.site.register(User)
    admin.site.register(Racer)
    admin.site.register(Team)
    admin.site.register(Race)
    admin.site.register(Statistic)
    admin.site.register(Comment)
