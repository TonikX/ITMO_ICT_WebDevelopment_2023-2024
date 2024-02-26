from django.contrib import admin
from .models import *


class Admin(admin.ModelAdmin):
    admin.site.register(User)
    admin.site.register(Item)
    admin.site.register(Warehouse)
    admin.site.register(Shipment)
    # admin.site.register(Inventory)
    admin.site.register(Nomenclature)
    admin.site.register(Comment)
