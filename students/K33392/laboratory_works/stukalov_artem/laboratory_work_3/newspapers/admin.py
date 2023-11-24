from django.contrib import admin
from . import models

admin.site.register(models.Newspaper)
admin.site.register(models.PrintingOffice)
admin.site.register(models.PostOffice)
admin.site.register(models.NewspaperDistribution)
admin.site.register(models.NewspaperEdition)
admin.site.register(models.NewspaperOrder)
