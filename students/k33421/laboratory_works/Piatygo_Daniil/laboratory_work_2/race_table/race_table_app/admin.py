from django.contrib import admin
from .models import Team, Racer, Race, RaceEntry, Comment

admin.site.register(Team)
admin.site.register(Racer)
admin.site.register(Race)
admin.site.register(RaceEntry)
admin.site.register(Comment)
