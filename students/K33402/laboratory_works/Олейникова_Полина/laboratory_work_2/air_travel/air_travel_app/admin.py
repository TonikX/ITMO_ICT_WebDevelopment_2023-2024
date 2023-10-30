from django.contrib import admin
from .models import Passenger, Flight, Seat, Reservation, Comment
from django.contrib.auth.admin import UserAdmin

admin.site.register(Passenger, UserAdmin)
admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Reservation)
admin.site.register(Comment)
