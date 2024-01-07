from django.urls import path

from hotel.views import *

urlpatterns = [
    path('checkins/<int:room_id>/<str:start_date>/<str:end_date>/', CheckinListView.as_view(), name='checkin-list'),
    path('guests/from_city/<str:city>/', GuestsFromCityView.as_view(), name='guests-from-city'),
    path('cleaner/for_guest/<int:guest_id>/<str:date>/', CleanerForGuestView.as_view(), name='cleaner-for-guest'),
    path('free_rooms/<str:date>/', FreeRoomsView.as_view(), name='free-rooms'),
    path('related_guests/<int:guest_id>/<str:start_date>/<str:end_date>/', RelatedGuestsListView.as_view(), name='related-guests-list'),
    path('quarterly_report/<str:start_date>/<str:end_date>/', HotelReportView.as_view(), name='quarterly_report'),
    path('hire_staff/', HireStaffView.as_view(), name='hire_staff'),
    path('fire_staff/', FireStaffView.as_view(), name='fire_staff'),
    path('add_cleaning/', AddCleaningView.as_view(), name='add_cleaning'),
    path('delete_cleaning/', DeleteCleaningView.as_view(), name='delete_cleaning'),
    path('checkin/', CheckinView.as_view(), name='checkin'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('guest_create/', GuestCreateView.as_view(), name='create_guest'),
    path('rooms/', RoomWithGuestListView.as_view(), name='room-with-guest-list'),
]