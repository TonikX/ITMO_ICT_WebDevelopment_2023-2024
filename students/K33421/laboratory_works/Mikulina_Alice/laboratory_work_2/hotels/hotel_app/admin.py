from django.contrib import admin
from .models import *


class CommentInline(admin.StackedInline):
    model = Review
    extra = 0

class ReservationAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Review)
admin.site.register(Reservation, ReservationAdmin)