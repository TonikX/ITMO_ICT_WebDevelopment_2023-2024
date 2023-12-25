from rest_framework import serializers
from .models import Room, Client, ClientInfo, Employee, Floor, Day, EmployeeFloor, EmployeeDay
from rest_framework import serializers
from .models import CustomUser, Room, Client, ClientInfo, Employee, Floor, Day, EmployeeFloor, EmployeeDay
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone')
        extra_kwargs = {'phone': {'required': False}}



    


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInfo
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    client_info = ClientInfoSerializer()

    class Meta:
        model = Client
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

class EmployeeFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeFloor
        fields = '__all__'

class EmployeeDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDay
        fields = '__all__'
