from django.contrib import admin

from .models import *

admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Reservation)
admin.site.register(Comment)
