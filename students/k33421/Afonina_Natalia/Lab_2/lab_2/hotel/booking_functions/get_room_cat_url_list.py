from django.urls import reverse
from hotel.models import Room


def get_room_cat_url_list():
    room = Room.objects.all()[0]
    room_cat_url_list = []
    room_categories = dict(room.ROOM_CATEGORIES)

    for category in room_categories:
        room_category = room_categories.get(category)
        room_url = reverse('hotel:RoomDetailView', kwargs={'category': category})
        room_cat_url_list.append((room_category, room_url))
    return room_cat_url_list

