from django.contrib import admin
from .models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(CarOwner)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(DriverLicense)
class LicenseAdmin(admin.ModelAdmin):
    pass


@admin.register(Ownership)
class OwnershipAdmin(admin.ModelAdmin):
    pass
