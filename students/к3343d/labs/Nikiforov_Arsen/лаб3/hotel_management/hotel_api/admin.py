from django.contrib import admin
from .models import (Room, Client, ClientInfo, Employee, Floor, Day, 
                     EmployeeFloor, EmployeeDay, Booking, CustomUser)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'floor', 'status', 'cost')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'start_date', 'end_date', 'confirmed']
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        for booking in queryset:
            booking.confirmed = True
            booking.room.booked_by = booking.user
            booking.room.set_occupied(True)  # Указываем True, что комната теперь занята
            booking.room.save()
            booking.save()
    confirm_booking.short_description = "Подтвердить выбранные бронирования"

    def cancel_booking(self, request, queryset):
        for booking in queryset:
            room = booking.room
            room.set_available()
            room.save()
            booking.delete()
    cancel_booking.short_description = "Отменить выбранные бронирования и установить комнату доступной"

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            room = obj.room
            room.set_available()
            room.save()
        queryset.delete()  # Удаляем все бронирования в выборке

    def delete_model(self, request, obj):
        room = obj.room
        room.set_available()
        room.save()
        obj.delete()

admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(ClientInfo)
admin.site.register(Employee)
admin.site.register(Floor)
admin.site.register(Day)
admin.site.register(EmployeeFloor)
admin.site.register(EmployeeDay)
