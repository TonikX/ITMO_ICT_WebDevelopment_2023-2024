from django.contrib import admin
from .models import Car, Ownership, Driver
from django.contrib.auth.admin import UserAdmin

admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(Driver)
