from django.contrib import admin
from .models import *


for model in [Driver, Car, Ownership, DriverLicence]:
    admin.site.register(model)
