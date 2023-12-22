# admin.py

``` 
from django.contrib import admin
from .models import Doctor, Cabinet, Patient, Appointment, Payment, MedicalService, Schedule


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty', 'date_of_start', 'date_of_end')
    search_fields = ('first_name', 'last_name', 'specialty')
    list_filter = ('date_of_start', 'date_of_end')
    date_hierarchy = 'date_of_start'

@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ('name', 'work_schedule', 'responsible', 'internal_phone')
    search_fields = ('name', 'responsible')
    list_filter = ('work_schedule',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'medical_card_number')
    search_fields = ('first_name', 'last_name', 'medical_card_number')
    list_filter = ('date_of_birth',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'cabinet', 'date_time', 'diagnosis')
    search_fields = ('doctor__first_name', 'doctor__last_name', 'patient__first_name', 'patient__last_name', 'diagnosis')
    list_filter = ('date_time',)
    date_hierarchy = 'date_time'

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount')
    search_fields = ('appointment__doctor__first_name', 'appointment__doctor__last_name', 'amount')
    list_filter = ('amount',)

@admin.register(MedicalService)
class MedicalServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_week', 'start_time', 'end_time')
    search_fields = ('doctor__first_name', 'doctor__last_name')
    list_filter = ('day_of_week', 'start_time', 'end_time')


```