from django.contrib import admin
from .models import Driver, Car, Ownership, DriverDocs


admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(DriverDocs)
admin.site.register(Ownership)