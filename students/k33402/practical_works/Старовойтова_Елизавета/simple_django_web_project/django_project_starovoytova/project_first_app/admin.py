from django.contrib import admin

from .models import Owner
from .models import Car
from .models import Ownership
from .models import DriverLicense
from .models import UserProfile


admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriverLicense)
admin.site.register(UserProfile)

