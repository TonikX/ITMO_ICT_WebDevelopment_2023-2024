from django.contrib import admin

# Register your models here.
#from races_app.models import User
from django.contrib.auth.models import Group

from races_table.models import Racer, Race, RaceConnection, Comment, User
admin.site.register(User)
admin.site.register(Racer)
admin.site.register(Race)
admin.site.register(RaceConnection)
admin.site.register(Comment)
user_group, created = Group.objects.get_or_create(name='Пользователь')
admin_group, created = Group.objects.get_or_create(name='Администратор')