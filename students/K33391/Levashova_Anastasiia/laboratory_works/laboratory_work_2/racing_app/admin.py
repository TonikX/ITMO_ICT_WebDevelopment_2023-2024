from django.contrib import admin
from .models import RacerCar, Racer, Race, RaceResult, Registration, Comment

admin.site.register(RacerCar)
admin.site.register(Racer)
admin.site.register(Race)
admin.site.register(RaceResult)
admin.site.register(Registration)
admin.site.register(Comment)
