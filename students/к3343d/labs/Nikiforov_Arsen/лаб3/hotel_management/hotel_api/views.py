from django.shortcuts import render
from .models import Room, Client, Employee, Floor, Day, EmployeeFloor, EmployeeDay, ClientInfo
from rest_framework import viewsets
from .serializers import RoomSerializer, ClientSerializer, EmployeeSerializer, FloorSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Room, Client, Employee, Floor, Day, EmployeeFloor, EmployeeDay, ClientInfo

def rooms_list(request):
    room_type_query = request.GET.get('room_type', '').strip()
    room_status_query = request.GET.get('room_status', '').strip()

    rooms = Room.objects.all()

    if room_type_query:
        rooms = rooms.filter(room_type__iexact=room_type_query)
    if room_status_query:
        rooms = rooms.filter(status__iexact=room_status_query)

    context = {
        'rooms': rooms,
        'selected_type': room_type_query,
        'selected_status': room_status_query,
    }
    return render(request, 'hotel_api/rooms_list.html', context)












def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'hotel_api/register.html', {'form': form})




@login_required
def home(request):
    return render(request, 'hotel_api/menu.html')



def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'hotel_api/client_list.html', {'clients': clients})


# для списка сотрудников
def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'hotel_api/employee_list.html', {'employees': employees})


def home(request):
    return render(request, 'hotel_api/menu.html')

def bookings_list(request):
    # Логика для списка бронирований
    return render(request, 'hotel_api/bookings_list.html')

def floors_list(request):
    floors = Floor.objects.all()
    return render(request, 'hotel_api/floor_list.html', {'floors': floors})

def staff_management(request):
    # Логика для управления персоналом
    return render(request, 'hotel_api/staff_management.html')

def reports(request):
    return render(request, 'hotel_api/reports.html')

def settings(request):
    return render(request, 'hotel_api/settings.html')

def client_info_list(request):
    client_info = ClientInfo.objects.all()
    return render(request, 'hotel_api/client_info_list.html', {'client_info': client_info})

# Добавленные представления для недостающих моделей

def days_list(request):
    days = Day.objects.all()
    return render(request, 'hotel_api/days_list.html', {'days': days})

def employee_floors_list(request):
    employee_floors = EmployeeFloor.objects.all()
    return render(request, 'hotel_api/employee_floors_list.html', {'employee_floors': employee_floors})

def employee_days_list(request):
    employee_days = EmployeeDay.objects.all()
    return render(request, 'hotel_api/employee_days_list.html', {'employee_days': employee_days})