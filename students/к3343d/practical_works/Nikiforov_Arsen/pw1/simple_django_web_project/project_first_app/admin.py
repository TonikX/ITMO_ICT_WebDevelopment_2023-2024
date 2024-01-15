from django.contrib import admin
from .models import Owner, Car, Ownership, DriverLicense, ExampleModel
from .models import CustomUser, OwnerProfile

admin.site.register(CustomUser)
admin.site.register(OwnerProfile)
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriverLicense)
admin.site.register(ExampleModel)

