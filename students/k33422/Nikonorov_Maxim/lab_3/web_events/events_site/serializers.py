from rest_framework import serializers
from django.utils import timezone
from .models import EventsUser, EventCard, EventTypeList, Place, UsersEventsList, SubscribedEmail

class EventsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsUser
        fields = ['id', 'username', 'LastName', 'FirstName', 'DateOfBirth', 'PhoneNumber', 'IsSubscribed']

class EventCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCard
        fields = ['id', 'PostTitle', 'EventType', 'Description', 'DateOfEvent', 'EventPlace', 'NumberOfParticipants', 'AgeRestriction', 'Status']

class EventTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTypeList
        fields = ['id', 'TypeTitle', 'Description', 'Colour']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'PlaceTitle', 'PlaceAddress', 'PlaceCapacity']

class UsersEventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersEventsList
        fields = ['id', 'EventUser', 'EventCard', 'TimeOfRegistration']

class SubscribedEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribedEmail
        fields = ['id', 'User', 'Email']

