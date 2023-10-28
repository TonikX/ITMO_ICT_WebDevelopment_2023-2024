from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from main.models import Tour, Reservation


content_type_tour = ContentType.objects.get_for_model(Tour)
content_type_reservation = ContentType.objects.get_for_model(Reservation)



view_tour_permission = Permission.objects.get(codename='view_tour', content_type=content_type_tour)
add_reservation_permission = Permission.objects.get(codename='add_reservation', content_type=content_type_reservation)
delete_reservation_permission = Permission.objects.get(codename='delete_reservation', content_type=content_type_reservation)
edit_reservation_permission = Permission.objects.get(codename='change_reservation', content_type=content_type_reservation)


user_group, created = Group.objects.get_or_create(name='Пользователь')
admin_group, created = Group.objects.get_or_create(name='Администратор')


user_group.permissions.set([view_tour_permission, add_reservation_permission, delete_reservation_permission])
admin_group.permissions.set([view_tour_permission, add_reservation_permission, delete_reservation_permission, edit_reservation_permission])

