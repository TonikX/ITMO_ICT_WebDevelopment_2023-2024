from django.contrib import admin
from .models import Owner, Car, Own, Driver_license

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Own)
admin.site.register(Driver_license)
