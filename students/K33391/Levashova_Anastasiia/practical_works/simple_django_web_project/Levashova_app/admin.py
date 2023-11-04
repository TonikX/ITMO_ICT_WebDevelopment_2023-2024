from django.contrib import admin
from .models import DriverLicense, CarOwner, Car, CarOwn

admin.site.register(DriverLicense)
admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(CarOwn)
