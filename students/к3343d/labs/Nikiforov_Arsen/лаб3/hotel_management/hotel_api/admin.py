from django.contrib import admin
from .models import (Room, Client, ClientInfo, Employee, Floor, Day, EmployeeFloor, 
                     EmployeeDay, Booking, CustomUser)

# Класс администратора для модели Room
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'floor', 'status', 'cost')

# Класс администратора для модели Booking 
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'start_date', 'end_date', 'confirmed']
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)
    confirm_booking.short_description = "Confirm selected bookings"

# Регистрация других моделей
admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(ClientInfo)
admin.site.register(Employee)
admin.site.register(Floor)
admin.site.register(Day)
admin.site.register(EmployeeFloor)
admin.site.register(EmployeeDay)
