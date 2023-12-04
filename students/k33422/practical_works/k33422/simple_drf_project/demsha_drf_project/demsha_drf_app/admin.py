from django.contrib import admin
from .models import CarOwner, License, Car, Ownership

admin.site.register(CarOwner)
admin.site.register(License)
admin.site.register(Ownership)
admin.site.register(Car)