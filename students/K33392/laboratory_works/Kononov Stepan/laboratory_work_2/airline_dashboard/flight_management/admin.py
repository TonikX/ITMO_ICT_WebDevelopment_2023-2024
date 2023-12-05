from django.contrib import admin

from flight_management.models import *

admin.site.register(User)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation)
admin.site.register(FlightReview)

