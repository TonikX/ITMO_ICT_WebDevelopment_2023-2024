from django.contrib import admin
from django.urls import path, include

from django.urls import path
from .views import (
    EventsUserListView, EventsUserDetailView,
    EventCardListView, EventCardDetailView,
    EventTypeListView,
    PlaceListView, PlaceDetailView,
    UsersEventsListView,
    SubscribedEmailListView,
    AboutListView, 
)

urlpatterns = [
    # EventsUser URLs
    path('events-users/', EventsUserListView.as_view(), name='events-user-list'),
    path('events-users/<int:pk>/', EventsUserDetailView.as_view(), name='events-user-detail'),

    # EventCard URLs
    path('event-cards/', EventCardListView.as_view(), name='event-card-list'),
    path('event-cards/<int:pk>/', EventCardDetailView.as_view(), name='event-card-detail'),

    # EventType URLs
    path('event-types/', EventTypeListView.as_view(), name='event-type-list'),

    # Place URLs
    path('places/', PlaceListView.as_view(), name='place-list'),
    path('places/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),

    # UsersEventsList URLs
    path('users-events/', UsersEventsListView.as_view(), name='users-events-list'),

    # SubscribedEmail URLs
    path('subscribed-emails/', SubscribedEmailListView.as_view(), name='subscribed-email-list'),

    # About URLs
    path('about/', AboutListView.as_view(), name='about-list'),
]
