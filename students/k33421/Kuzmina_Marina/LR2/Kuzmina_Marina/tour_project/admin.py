from django.contrib import admin
from .models import Tour, Reservation, Review

#admin.site.register(Tour)
admin.site.register(Reservation)
admin.site.register(Review)

class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'agency', 'description', 'start_date', 'end_date', 'payment_conditions', 'is_sold']

admin.site.register(Tour, TourAdmin)
