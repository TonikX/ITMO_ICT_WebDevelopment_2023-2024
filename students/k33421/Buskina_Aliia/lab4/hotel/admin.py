from django.contrib import admin

from .models import Room, Guest, Cleaning, Staff, Checkin

admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Cleaning)
admin.site.register(Staff)
admin.site.register(Checkin)
