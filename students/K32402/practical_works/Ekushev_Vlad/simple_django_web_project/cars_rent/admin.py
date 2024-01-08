from django.contrib import admin
from .models import Driver, Car, Ownership, DriverLicence

admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriverLicence)
