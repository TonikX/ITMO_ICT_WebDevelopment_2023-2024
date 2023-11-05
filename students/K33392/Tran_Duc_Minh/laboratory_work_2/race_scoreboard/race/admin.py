from django.contrib import admin
from .models import Team, Participant, Race, Commentator, Comment, RaceRegistration, RaceResult

admin.site.register(Team)
admin.site.register(Participant)
admin.site.register(Race)
admin.site.register(Commentator)
admin.site.register(Comment)
admin.site.register(RaceRegistration)
admin.site.register(RaceResult)