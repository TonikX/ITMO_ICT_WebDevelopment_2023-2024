from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Conference)
admin.site.register(Performance)
admin.site.register(Review)
