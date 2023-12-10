from rest_framework import generics
from django.db.models import Count
from .models import EventsUser, EventCard, EventTypeList, Place, UsersEventsList, SubscribedEmail
from .serializers import (
    EventsUserSerializer, EventCardSerializer, EventTypeListSerializer,
    PlaceSerializer, UsersEventsListSerializer, SubscribedEmailSerializer
)

class EventsUserListView(generics.ListCreateAPIView):
    queryset = EventsUser.objects.all()
    serializer_class = EventsUserSerializer

class EventsUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventsUser.objects.all()
    serializer_class = EventsUserSerializer

class EventCardListView(generics.ListCreateAPIView):
    queryset = EventCard.objects.all()
    serializer_class = EventCardSerializer

class EventCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventCard.objects.all()
    serializer_class = EventCardSerializer

class EventTypeListView(generics.ListCreateAPIView):
    queryset = EventTypeList.objects.all()
    serializer_class = EventTypeListSerializer

class PlaceListView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class UsersEventsListView(generics.ListAPIView):
    queryset = UsersEventsList.objects.all()
    serializer_class = UsersEventsListSerializer
    
    def get(self, request, *args, **kwargs):
        event_registrations = UsersEventsList.objects.values('EventCard').annotate(registrations_count=Count('EventCard'))

        for registration in event_registrations:
            event_card_id = registration['EventCard']
            registrations_count = registration['registrations_count']
            print(f"Event {event_card_id}: registered {registrations_count} user(s)")
            
        return super().get(request, *args, **kwargs)
        
class SubscribedEmailListView(generics.ListAPIView):
    queryset = SubscribedEmail.objects.all()
    serializer_class = SubscribedEmailSerializer



