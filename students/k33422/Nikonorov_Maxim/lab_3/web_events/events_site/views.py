from rest_framework import generics
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from .models import EventsUser, EventCard, EventTypeList, Place, UsersEventsList, SubscribedEmail
from .serializers import (
    EventsUserSerializer, EventCardSerializer, EventTypeListSerializer,
    PlaceSerializer, UsersEventsListSerializer, SubscribedEmailSerializer,
    EventParticipantsSerializer, UsersEventsListViewSerializer
)

from rest_framework.response import Response
from rest_framework import status

class UsersEventsListWideView(generics.ListAPIView):
    queryset = UsersEventsList.objects.all()
    serializer_class = UsersEventsListViewSerializer
    
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

class UsersEventsListView(generics.ListCreateAPIView):
    queryset = UsersEventsList.objects.all()
    serializer_class = UsersEventsListSerializer
    
class UsersEventsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsersEventsList.objects.all()
    serializer_class = UsersEventsListSerializer
    
class SubscribedEmailListView(generics.ListAPIView):
    queryset = SubscribedEmail.objects.all()
    serializer_class = SubscribedEmailSerializer
    
class EventParticipantsView(generics.ListAPIView):
    serializer_class = EventParticipantsSerializer

    def get_queryset(self):
        events = EventCard.objects.all()

        participants_list = []
        for event in events:
            participants = event.events_users_list.all()
            participants_ = {'EventID': event.id, 'Participants': participants}
            participants_list.append(participants_)

        return participants_list
    
class CurrentUserView(APIView):
    def get(self, request):
        serializer = EventsUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UsersEventsListDeleteView(DestroyAPIView):
    queryset = UsersEventsList.objects.all()
    serializer_class = UsersEventsListSerializer
    lookup_field = 'pk'  