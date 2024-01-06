from django.contrib import admin

from .models import Flight, Reservation, Airline, Review

admin.site.register(Flight)
admin.site.register(Reservation)
admin.site.register(Airline)
admin.site.register(Review)
