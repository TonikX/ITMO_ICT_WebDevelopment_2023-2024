### serializers.py

```python
from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class FreeRoomsSerializer(serializers.Serializer):
    date = serializers.DateField()
    free_rooms_count = serializers.IntegerField()

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['name', 'surname']

class CleaningSerializer(serializers.ModelSerializer):
    cleaner = StaffSerializer(source='staff_id', read_only=True)  # Используем source для указания связи с staff_id

    class Meta:
        model = Cleaning
        fields = '__all__'
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = '__all__'

class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = '__all__'

class RelatedGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'surname', 'hometown']

class RelatedGuestsListSerializer(serializers.Serializer):
    date = serializers.DateField()
    guests = RelatedGuestSerializer(many=True)

class RelatedGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'surname', 'hometown']

class RelatedGuestsListSerializer(serializers.Serializer):
    date = serializers.DateField()
    guests = RelatedGuestSerializer(many=True)

class ReportSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    guests_count = serializers.IntegerField()
    floor = serializers.IntegerField(source='room_id__floor')
    room_type = serializers.CharField(source='room_id__type')
    room_income = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_income = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['total_income'] = self.context['total_income']
        return data

```