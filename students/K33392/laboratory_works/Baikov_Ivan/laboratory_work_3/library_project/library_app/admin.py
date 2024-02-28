from django.contrib import admin
from library_app import models

admin.site.register(models.Book)
admin.site.register(models.Reader)
admin.site.register(models.Hall)
admin.site.register(models.Ownership)
admin.site.register(models.Availability)

