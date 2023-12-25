from rest_framework import serializers
from .models import Room, Client, ClientInfo, Employee, Floor, Day, EmployeeFloor, EmployeeDay
from .models import CustomUser, Room, Client, ClientInfo, Employee, Floor, Day, EmployeeFloor, EmployeeDay
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Floor, Room

#/api/floor_occupancy/
class FloorOccupancySerializer(serializers.ModelSerializer):
    occupied_rooms_count = serializers.SerializerMethodField()

    class Meta:
        model = Floor
        fields = ['number', 'occupied_rooms_count']

    def get_occupied_rooms_count(self, floor):
        # Считаем количество занятых комнат на этаже
        return Room.objects.filter(floor=floor, status='occupied').count()










class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  

        

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInfo
        fields = '__all__'







#Создание сериализатора для вложенного запроса:
class NestedClientSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    client_info = ClientInfoSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'room', 'client_info']





class EmployeeFloorSerializer(serializers.ModelSerializer):
    # Добавлю сюда сериализатор для Employee
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = EmployeeFloor
        fields = ['employee', 'floor', 'room'] 



"""""
 сложный запрос:
Получить список всех комнат, которые заняты, 
вместе с информацией о клиентах, проживающих в них, 
и сотрудниках, ответственных за уборку комнаты.
"""""
class ComplexRoomSerializer(serializers.ModelSerializer):
    clients = NestedClientSerializer(many=True, read_only=True)
    
    #используем сериализатор для EmployeeFloor вместо Employee
    employees = EmployeeFloorSerializer(source='employee_floor_set', many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'room_type', 'status', 'cost', 'floor', 'clients', 'employees']








User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone')
        extra_kwargs = {'phone': {'required': False}}



    




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


    class Meta:
        model = Client
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
