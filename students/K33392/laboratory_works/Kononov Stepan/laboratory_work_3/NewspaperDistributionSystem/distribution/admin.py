from django.contrib import admin

from distribution.models import *

admin.site.register(Editor)
admin.site.register(PrintingHouse)
admin.site.register(Newspaper)
admin.site.register(PrintRun)
admin.site.register(PostOffice)
admin.site.register(PostalArrival)

