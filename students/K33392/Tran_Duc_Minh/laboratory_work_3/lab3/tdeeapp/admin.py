from django.contrib import admin
from .models import Activity, Food, Profile, DailyData, UserFood

# Register your models here.
admin.site.register(Activity)
admin.site.register(Food)
admin.site.register(Profile)
admin.site.register(DailyData)
admin.site.register(UserFood)


