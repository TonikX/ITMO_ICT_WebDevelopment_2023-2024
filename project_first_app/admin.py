from django.contrib import admin
from .models import AutoOwner, Auto, Ownership, Licence

admin.site.register(AutoOwner)
admin.site.register(Auto)
admin.site.register(Ownership)
admin.site.register(Licence)