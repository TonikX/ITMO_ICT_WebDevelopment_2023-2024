from rest_framework import generics
from .models import EventsUser, EventCard, EventTypeList, Place, UsersEventsList, SubscribedEmail, About
from .serializers import (
    EventsUserSerializer, EventCardSerializer, EventTypeListSerializer,
    PlaceSerializer, UsersEventsListSerializer, SubscribedEmailSerializer, AboutSerializer
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

class EventTypeListView(generics.ListAPIView):
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

class SubscribedEmailListView(generics.ListAPIView):
    queryset = SubscribedEmail.objects.all()
    serializer_class = SubscribedEmailSerializer

class AboutListView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


