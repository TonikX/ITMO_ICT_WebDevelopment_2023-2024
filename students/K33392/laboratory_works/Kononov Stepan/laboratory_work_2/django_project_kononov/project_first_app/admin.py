from django.contrib import admin

from project_first_app.models import CarOwner, Car, Ownership, DrivingLicense

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DrivingLicense)
