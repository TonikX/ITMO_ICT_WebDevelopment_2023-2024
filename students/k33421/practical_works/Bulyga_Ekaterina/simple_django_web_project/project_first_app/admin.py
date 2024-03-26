from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Owning)
admin.site.register(License)
