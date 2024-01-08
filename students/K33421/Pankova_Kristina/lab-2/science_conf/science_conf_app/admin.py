from django.contrib import admin
from .models import *

admin.site.register(ConferenceGuest)
admin.site.register(Conference)
admin.site.register(ConferenceAttendance)
admin.site.register(ConferenceComments)
admin.site.register(ConferenceLectures)

