from django.contrib import admin
from .models import User, License, Car, Ownership

admin.site.register(User)
admin.site.register(License)
admin.site.register(Ownership)
admin.site.register(Car)
