from django.contrib import admin
from .models import *


@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    pass

