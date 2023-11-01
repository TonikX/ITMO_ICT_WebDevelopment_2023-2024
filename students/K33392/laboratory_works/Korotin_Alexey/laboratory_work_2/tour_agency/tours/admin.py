from django.contrib import admin
from .models import Tour, Reservation, Review


@admin.register(Tour)
class AdminTourView(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class AdminReservationView(admin.ModelAdmin):
    pass


@admin.register(Review)
class AdminReviewView(admin.ModelAdmin):
    pass
