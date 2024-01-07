from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.Passenger, UserAdmin)
admin.site.register(models.Hotel)
admin.site.register(models.TypeOfRoom)
admin.site.register(models.Room)
admin.site.register(models.Reservation)
admin.site.register(models.Comment)