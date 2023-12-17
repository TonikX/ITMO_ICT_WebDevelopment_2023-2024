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
    EventParticipantsView
)

urlpatterns = [
    path('users/', EventsUserListView.as_view(), name='events-user-list'),
    path('users/<int:pk>/', EventsUserDetailView.as_view(), name='events-user-detail'),

    path('events/', EventCardListView.as_view(), name='event-card-list'),
    path('events/<int:pk>/', EventCardDetailView.as_view(), name='event-card-detail'),

    path('event-types/', EventTypeListView.as_view(), name='event-type-list'),

    path('places/', PlaceListView.as_view(), name='place-list'),
    path('places/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),

    path('users-events/', UsersEventsListView.as_view(), name='users-events-list'),
    path('event-list/', EventParticipantsView.as_view(), name='event-card-list'),
    
    path('subscribed-emails/', SubscribedEmailListView.as_view(), name='subscribed-email-list'),
]
