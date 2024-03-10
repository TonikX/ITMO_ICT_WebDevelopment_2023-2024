from django.contrib import admin
from .models import *


admin.site.register(Company)
admin.site.register(BrokerCompany)
admin.site.register(Broker)
admin.site.register(Product)
admin.site.register(ProductByCompany)
admin.site.register(Consignment)