from django.contrib import admin
from .models import *

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(DriversLicence)
admin.site.register(CarOwnership)

