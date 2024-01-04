from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Room, Client, ClientInfo, Employee, Floor, Day, EmployeeFloor, EmployeeDay, Booking, CustomUser
from .models import Review



User = get_user_model()

class RoomSerializer(serializers.ModelSerializer):
    current_occupant = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Room
        fields = '__all__'

class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInfo
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class EmployeeDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDay
        fields = '__all__'

class EmployeeFloorSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = EmployeeFloor
        fields = ['employee', 'floor', 'room']

class NestedClientSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    client_info = ClientInfoSerializer(read_only=True)
    class Meta:
        model = Client
        fields = ['id', 'room', 'client_info']

class ComplexRoomSerializer(serializers.ModelSerializer):
    clients = NestedClientSerializer(many=True, read_only=True)
    employees = EmployeeFloorSerializer(source='employee_floor_set', many=True, read_only=True)
    booked_by = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['id', 'room_type', 'status', 'cost', 'floor', 'clients', 'employees', 'booked_by']

    def get_booked_by(self, obj):
        return obj.booked_by.username if obj.booked_by else None


class ClientSerializer(serializers.ModelSerializer):
    client_info = ClientInfoSerializer()
    class Meta:
        model = Client
        fields = '__all__'
    def create(self, validated_data):
        client_info_data = validated_data.pop('client_info')
        client_info = ClientInfo.objects.create(**client_info_data)
        client = Client.objects.create(client_info=client_info, **validated_data)
        return client

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone')
        extra_kwargs = {'phone': {'required': False}}

class BookingSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    room_details = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'start_date', 'end_date', 'confirmed', 'user_details', 'room_details']

    def get_user_details(self, obj):
        return UserSerializer(obj.user).data

    def get_room_details(self, obj):
        return RoomSerializer(obj.room).data


class FloorOccupancySerializer(serializers.ModelSerializer):
    occupied_rooms_count = serializers.SerializerMethodField()
    class Meta:
        model = Floor
        fields = ['number', 'occupied_rooms_count']
    def get_occupied_rooms_count(self, floor):
        return Room.objects.filter(floor=floor, status='occupied').count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author', 'text', 'created_at']
