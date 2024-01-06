from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        "email",
        "passport_number",
        "home_address",
        "nationality",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",
            {"fields": ("passport_number", "home_address", "nationality")},
        ),
    )


admin.site.register(Car)
admin.site.register(CarOwner)
admin.site.register(Ownership)
admin.site.register(DriveLicense)
admin.site.register(CustomUser, CustomUserAdmin)
