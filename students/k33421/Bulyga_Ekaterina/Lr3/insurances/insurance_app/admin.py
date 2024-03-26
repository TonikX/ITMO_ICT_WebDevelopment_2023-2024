from django.contrib import admin
from .models import *

admin.site.register(Individual)
admin.site.register(Type)
admin.site.register(Employee)
admin.site.register(Organization)
admin.site.register(InsureOrganization)
admin.site.register(InsureAgent)
admin.site.register(Contract)
admin.site.register(InsuranceCase)
