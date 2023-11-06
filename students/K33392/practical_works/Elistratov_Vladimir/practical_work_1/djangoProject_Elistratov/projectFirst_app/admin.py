from django.contrib import admin

from .models import CarOwner
from .models import Car
from .models import Treaty
from .models import OwnerDocument

class Admin(admin.ModelAdmin):
    #Register your models here.
    admin.site.register(CarOwner)
    admin.site.register(Car)
    admin.site.register(Treaty)
    admin.site.register(OwnerDocument)