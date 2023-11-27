from django.contrib import admin

from .models import Guest, Hotel, Room, Booking, Review


admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)
