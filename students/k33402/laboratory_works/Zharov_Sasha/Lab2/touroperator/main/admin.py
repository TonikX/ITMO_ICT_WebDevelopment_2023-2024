from django.contrib import admin
from .models import Tour, User, Reservation, TourComment

admin.site.register(Tour)
admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(TourComment)
