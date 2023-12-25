# admin.py
from django.contrib import admin
from django import forms
from .models import Room, Client, ClientInfo, Employee, Floor, Day, EmployeeFloor, EmployeeDay
from .models import CustomUser



class RoomAdminForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_type': forms.Select(choices=Room.ROOM_TYPES)
        }

class RoomAdmin(admin.ModelAdmin):
    form = RoomAdminForm
    
admin.site.register(CustomUser)
admin.site.register(Room, RoomAdmin)
admin.site.register(Client)
admin.site.register(ClientInfo)
admin.site.register(Employee)
admin.site.register(Floor)
admin.site.register(Day)
admin.site.register(EmployeeFloor)
admin.site.register(EmployeeDay)
