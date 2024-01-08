from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(SalonOwner)
admin.site.register(Salon)
admin.site.register(SalonComments)
admin.site.register(SalonService)
admin.site.register(SalonAppointment)
admin.site.register(SalonServiceComments)

