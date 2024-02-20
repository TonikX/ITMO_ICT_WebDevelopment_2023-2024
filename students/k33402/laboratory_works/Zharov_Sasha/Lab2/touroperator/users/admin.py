from django.contrib import admin
from django.contrib.auth.models import Group


user_group, created = Group.objects.get_or_create(name='Пользователь')
admin_group, created = Group.objects.get_or_create(name='Администратор')


