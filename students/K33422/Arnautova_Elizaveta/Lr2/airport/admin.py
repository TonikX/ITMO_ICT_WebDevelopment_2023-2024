from django.contrib import admin

# Register your models here.
from .models import Flight, Reservation, Review

admin.site.register(Flight)
admin.site.register(Reservation)
admin.site.register(Review)
