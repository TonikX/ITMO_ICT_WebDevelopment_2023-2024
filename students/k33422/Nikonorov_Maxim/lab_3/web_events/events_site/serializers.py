from rest_framework import serializers
from django.utils import timezone
from .models import EventsUser, EventCard, EventTypeList, Place, UsersEventsList, SubscribedEmail

class EventsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsUser
        fields = ['id', 'username', 'LastName', 'FirstName', 'DateOfBirth', 'PhoneNumber', 'IsSubscribed']

class EventTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTypeList
        fields = ['id', 'TypeTitle', 'Description', 'Colour']
        

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'PlaceTitle', 'PlaceAddress', 'PlaceCapacity']

class EventCardSerializer(serializers.ModelSerializer):
    EventType = EventTypeListSerializer()
    EventPlace = PlaceSerializer()
    
    class Meta:
        model = EventCard
        fields = ['id', 'PostTitle', 'EventType', 'Description', 'DateOfEvent', 'EventPlace', 'NumberOfParticipants', 'AgeRestriction', 'Status']


class UsersEventsListViewSerializer(serializers.ModelSerializer):
    EventUser = EventsUserSerializer()
    EventCard = EventCardSerializer()

    class Meta:
        model = UsersEventsList
        fields = ['EventUser', 'EventCard', 'TimeOfRegistration']
    
class UsersEventsListSerializer(serializers.ModelSerializer):
    
    EventUser = serializers.PrimaryKeyRelatedField(queryset=EventsUser.objects.all())
    EventCard = serializers.PrimaryKeyRelatedField(queryset=EventCard.objects.all())

    class Meta:
        model = UsersEventsList
        fields = ['EventUser', 'EventCard', 'TimeOfRegistration']

    def create(self, validated_data):
        event_user = validated_data.pop('EventUser')
        event_card = validated_data.pop('EventCard')

        user_event, created = UsersEventsList.objects.get_or_create(
            EventUser=event_user,
            EventCard=event_card,
            defaults=validated_data
        )

        return user_event

class SubscribedEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribedEmail
        fields = ['id', 'User', 'Email']
        
class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersEventsList
        fields = ['EventUser']

class EventParticipantsSerializer(serializers.Serializer):
    EventID = serializers.IntegerField()
    Participants = EventRegistrationSerializer(many=True)
    TotalParticipants = serializers.SerializerMethodField()

    def get_TotalParticipants(self, obj):
        return len(obj['Participants'])


