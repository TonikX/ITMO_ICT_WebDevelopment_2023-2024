from django.contrib import admin
from .models import *


# Register your models here.
class Admin(admin.ModelAdmin):
    admin.site.register(Person)
    admin.site.register(Treaty)
    admin.site.register(Tour)
    admin.site.register(Comments)
