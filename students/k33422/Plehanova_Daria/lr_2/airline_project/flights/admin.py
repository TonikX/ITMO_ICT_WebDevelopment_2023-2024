from django.contrib import admin
from . import models


admin.site.register(models.Reservation)
admin.site.register(models.Airplane)
admin.site.register(models.Airline)
admin.site.register(models.Flight)
admin.site.register(models.Ticket)
