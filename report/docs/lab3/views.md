### Сериалайзеры

Вторым шагом стало создание сериалайзеров, которые бы обеспечивали преобразование данных в удобное нам представление. Для этого я создал отдельный файл, где прописал все потенциальные сериалайзеры, к которым может иметь доступ администратор и пользователь.

``` py title="serializers.py"
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
```

### Представления

После прописания всех сериалайзеров необходимо создать представления, чтобы мы могли в интеравтивном режиме просматривать или изменять записи.

``` py title="views.py"
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
``` 

### Проверка работы

После указания всех url в файле `urls.py` можно проверять работоспособность кода.

