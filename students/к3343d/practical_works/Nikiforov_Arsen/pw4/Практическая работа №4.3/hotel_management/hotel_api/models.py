from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    phone = models.CharField("Телефон", max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.username


class Floor(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f"Floor {self.number}"

class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    )
    ROOM_STATUSES = (
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('cleaning', 'Cleaning'),
    )
    room_type = models.CharField(max_length=100, choices=ROOM_TYPES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rooms')
    status = models.CharField(max_length=100, choices=ROOM_STATUSES)




    def __str__(self):
        return f"{self.get_room_type_display()} on Floor {self.floor.number}"

class ClientInfo(models.Model):
    passport_number = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    check_in_date = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Client(models.Model):
    client_info = models.ForeignKey(ClientInfo, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='clients')

    def __str__(self):
        return f"Client {self.client_info.first_name} {self.client_info.last_name}"

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EmployeeFloor(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='employee_floor_set')  # связал с комнатами


    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} on Floor {self.floor.number}"

class EmployeeDay(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} on {self.day.name}"
