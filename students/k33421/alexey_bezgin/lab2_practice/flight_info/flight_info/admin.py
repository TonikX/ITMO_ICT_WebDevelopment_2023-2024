from django.contrib import admin

from .models import Flight, Reservation, AppUser, Review

admin.site.register(Flight)
admin.site.register(Reservation)
admin.site.register(AppUser)
admin.site.register(Review)
