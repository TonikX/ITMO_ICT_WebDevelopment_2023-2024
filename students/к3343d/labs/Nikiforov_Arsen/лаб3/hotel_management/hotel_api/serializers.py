from rest_framework import serializers
from .models import Room, Client, ClientInfo, Employee, Floor, Day, EmployeeFloor, EmployeeDay

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
