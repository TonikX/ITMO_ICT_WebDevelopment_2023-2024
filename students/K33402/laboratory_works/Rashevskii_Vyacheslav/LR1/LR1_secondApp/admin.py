from django.contrib import admin
from LR1_secondApp.models import *


class DisksAdmin(admin.ModelAdmin):
    list_display = ("id", "prod_date", "firm")


class GamesAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "author", "disk")


class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "sale_date", "sale_quantity", "disk", "sale_price")


class AdmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "admission_date", "admission_quantity", "disk", "admission_price")


class Sale_pointAdmin(admin.ModelAdmin):
    list_display = ("id", "sale_point_name", "sale_point_address", "number_of_stuff", "sale_id")


class Admission_pointAdmin(admin.ModelAdmin):
    list_display = ("id", "admission_point_name", "admission_point_address", "number_of_stuff", "admission_id")


admin.site.register(Disks,            DisksAdmin)
admin.site.register(Games,            GamesAdmin)
admin.site.register(Sale,             SaleAdmin)
admin.site.register(Admission,        AdmissionAdmin)
admin.site.register(Sale_point,       Sale_pointAdmin)
admin.site.register(Admission_point,  Admission_pointAdmin)
