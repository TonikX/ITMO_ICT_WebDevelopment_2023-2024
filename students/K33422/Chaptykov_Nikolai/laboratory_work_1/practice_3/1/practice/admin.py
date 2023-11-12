from django.contrib import admin
from practice.models import CarOwner, Ownership, Car, DriverLicence

# Register your models here.
admin.site.register(CarOwner)
admin.site.register(Ownership)
admin.site.register(Car)
admin.site.register(DriverLicence)

