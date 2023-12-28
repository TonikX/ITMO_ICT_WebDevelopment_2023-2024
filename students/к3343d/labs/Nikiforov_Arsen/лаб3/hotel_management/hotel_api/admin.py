from django.contrib import admin
from .models import (Room, Client, ClientInfo, Employee, Floor, Day, 
                     EmployeeFloor, EmployeeDay, Booking, CustomUser)

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
        for booking in queryset:
            booking.confirmed = True
            booking.room.set_occupied()  # Меняем статус комнаты на 'occupied'
            booking.save()
    confirm_booking.short_description = "Confirm selected bookings"

    def cancel_booking(self, request, queryset):
        for booking in queryset:
            room = booking.room
            room.set_available()
            room.save()
            booking.delete()
    cancel_booking.short_description = "Cancel selected bookings and set room available"

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            room = obj.room
            room.set_available()
            room.save()
        queryset.delete()  # This deletes all bookings in the queryset

    def delete_model(self, request, obj):
        room = obj.room
        room.set_available()
        room.save()
        obj.delete()

# Регистрация других моделей
admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(ClientInfo)
admin.site.register(Employee)
admin.site.register(Floor)
admin.site.register(Day)
admin.site.register(EmployeeFloor)
admin.site.register(EmployeeDay)
