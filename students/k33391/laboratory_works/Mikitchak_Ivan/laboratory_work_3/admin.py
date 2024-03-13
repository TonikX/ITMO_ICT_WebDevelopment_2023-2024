from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Agent)
admin.site.register(NaturalPerson)
admin.site.register(Specialization)
admin.site.register(LegalPerson)
admin.site.register(Employee)
admin.site.register(NaturalPersonContract)
admin.site.register(LegalPersonContract)
admin.site.register(InsuredEvent)
