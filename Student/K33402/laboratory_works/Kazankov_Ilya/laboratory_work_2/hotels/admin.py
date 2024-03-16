from django.contrib import admin

from .models import *

admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)