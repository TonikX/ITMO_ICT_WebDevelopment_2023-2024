from django.contrib import admin
from .models import Tour, Reservation, Review
from .models import Agency


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'agency', 'description', 'start_date', 'end_date', 'payment_conditions', 'country')
    search_fields = ('name', 'agency__name')
    list_filter = ('start_date', 'end_date', 'agency')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('tour', 'user', 'is_confirmed')
    list_filter = ('is_confirmed', 'tour', 'user')
    search_fields = ('tour__name', 'user__username')
    actions = ['confirm_reservation']

    def confirm_reservation(self, request, queryset):
        queryset.update(status='confirmed')
        self.message_user(request, "Выбранные бронирования были успешно подтверждены.")
    confirm_reservation.short_description = 'Подтвердить выбранные бронирования'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('tour', 'user', 'rating', 'text', 'comment_date')
    list_filter = ('rating', 'tour', 'user')
    search_fields = ('tour__name', 'user__username', 'text')


admin.site.register(Agency)
