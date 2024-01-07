from django.contrib import admin

from .models import Crew, CrewMember, AirlineCompany, Airplane, Route, Flight

admin.site.register(Crew)
admin.site.register(CrewMember)
admin.site.register(AirlineCompany)
admin.site.register(Airplane)
admin.site.register(Route)
admin.site.register(Flight)