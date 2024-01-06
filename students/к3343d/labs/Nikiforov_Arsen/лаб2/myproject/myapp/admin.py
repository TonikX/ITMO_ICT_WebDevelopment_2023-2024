from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Agency, Tour, Users, Reservation, Review

admin.site.register(Agency)
admin.site.register(Tour)

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

admin.site.register(Users, CustomUserAdmin)

admin.site.register(Reservation)
admin.site.register(Review)
