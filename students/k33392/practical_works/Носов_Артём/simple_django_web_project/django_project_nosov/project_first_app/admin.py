from django.contrib import admin

from .models import Owner, Dog, Exhibition, Participate

admin.site.register(Owner)
admin.site.register(Dog)
admin.site.register(Exhibition)
admin.site.register(Participate)