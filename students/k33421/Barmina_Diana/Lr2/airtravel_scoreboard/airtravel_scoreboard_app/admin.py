from django.contrib import admin
from .models import Traveler, Flight, Ticket, Plane, Seat, Comment
# Register your models here.

admin.site.register(Ticket)
admin.site.register(Traveler)
admin.site.register(Flight)
admin.site.register(Plane)
admin.site.register(Seat)
admin.site.register(Comment)