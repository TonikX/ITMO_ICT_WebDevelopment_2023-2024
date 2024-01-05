from django.contrib import admin
from .models import Hotel, RoomType, Reservation, Review, Visitor, Amenity

admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(Reservation)
admin.site.register(Review)
admin.site.register(Visitor)
admin.site.register(Amenity)
