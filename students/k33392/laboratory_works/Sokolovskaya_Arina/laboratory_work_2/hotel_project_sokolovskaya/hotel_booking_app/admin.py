from django.contrib import admin

from hotel_booking_app.models import *

# Register your models here.

admin.site.register(Hotel)
admin.site.register(Guest)
admin.site.register(Booking)
admin.site.register(Feedback)
admin.site.register(Room)

