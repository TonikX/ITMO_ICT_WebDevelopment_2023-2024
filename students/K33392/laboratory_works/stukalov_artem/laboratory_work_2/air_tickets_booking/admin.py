from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.User)
admin.site.register(models.AirLine)
admin.site.register(models.City)
admin.site.register(models.PlaneModel)
admin.site.register(models.Flight)
admin.site.register(models.Ticket)
