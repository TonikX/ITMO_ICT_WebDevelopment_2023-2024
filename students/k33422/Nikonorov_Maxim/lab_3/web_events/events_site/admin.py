from django.contrib import admin
from .models import EventsUser, EventCard, UsersEventsList, EventTypeList, SubscribedEmail, Place

admin.site.register(EventsUser)
admin.site.register(EventCard)
admin.site.register(UsersEventsList)
admin.site.register(EventTypeList)
admin.site.register(SubscribedEmail)
admin.site.register(Place)