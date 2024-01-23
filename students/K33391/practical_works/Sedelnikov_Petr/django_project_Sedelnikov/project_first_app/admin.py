from django.contrib import admin
from . import models

admin.site.register(models.CarOwner)
admin.site.register(models.Car)
admin.site.register(models.Ownership)
admin.site.register(models.DriverLicense)
