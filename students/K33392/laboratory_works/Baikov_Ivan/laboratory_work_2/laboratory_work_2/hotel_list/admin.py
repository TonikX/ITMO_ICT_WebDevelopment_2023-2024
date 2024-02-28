from django.contrib import admin
from .models import Hotel, Reservation, Review, Profile

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address', 'price', 'capacity')
    list_filter = ('owner',)
    search_fields = ('name', 'owner')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'check_in_date', 'check_out_date')
    list_filter = ('user', 'hotel', 'check_in_date', 'check_out_date')
    search_fields = ('user__username', 'hotel__name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'check_in_date', 'rating')
    list_filter = ('user', 'hotel', 'check_in_date', 'rating')
    search_fields = ('user__username', 'hotel__name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
