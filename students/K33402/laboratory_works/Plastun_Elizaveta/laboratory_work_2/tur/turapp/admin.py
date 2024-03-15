from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Tour, User, Reservation, TourComment

admin.site.register(Tour)
admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(TourComment)
user_group, created = Group.objects.get_or_create(name='Пользователь')
admin_group, created = Group.objects.get_or_create(name='Администратор')
