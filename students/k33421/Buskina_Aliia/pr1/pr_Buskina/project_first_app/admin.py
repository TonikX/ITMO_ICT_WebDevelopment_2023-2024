from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Car, CarOwner, DriverLicense, Ownership

admin.site.register(Car)
admin.site.register(CarOwner)
admin.site.register(DriverLicense)
admin.site.register(Ownership)