from django.contrib import admin
from .models import Driver, Auto, Ownership, OwnerDocs


admin.site.register(Driver)
admin.site.register(Auto)
admin.site.register(Ownership)
admin.site.register(OwnerDocs)

