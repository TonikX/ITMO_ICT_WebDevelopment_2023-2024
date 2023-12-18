from django.contrib import admin
from .models import Owner, Car, DrivingLicense, Ownership


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'birth_date')
    search_fields = ('last_name', 'first_name')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'registration_number', 'brand', 'model', 'color')
    search_fields = ('registration_number', 'brand', 'model')

@admin.register(DrivingLicense)
class DrivingLicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'license_number', 'license_type', 'issue_date')
    search_fields = ('owner__last_name', 'owner__first_name', 'license_number')

@admin.register(Ownership)
class OwnershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'car', 'start_date', 'end_date')
    search_fields = ('owner__last_name', 'car__registration_number')
