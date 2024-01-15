from django.contrib import admin

from .forms import NewPassengerForm
from .models import CustomUser, Flight, Booking

admin.site.register(CustomUser)
admin.site.register(Flight)
admin.site.register(Booking)
