### views.py


# Обзор views.py

Файл `views.py` содержит определения представлений для обработки запросов пользователей. Он включает в себя как функциональные, так и классовые представления.

## Импорты

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Room, Client, Employee, Floor, Day, EmployeeFloor, EmployeeDay, ClientInfo
from rest_framework import viewsets
from .serializers import RoomSerializer, ClientSerializer, EmployeeSerializer, FloorSerializer, DaySerializer, EmployeeFloorSerializer, EmployeeDaySerializer, ClientInfoSerializer
```

Эти импорты включают функции и классы Django для работы с представлениями, аутентификацией и моделями.

## Представления

```python
@login_required(login_url='/login/') 
def home(request):
    return render(request, 'hotel_api/home.html')
```

Это представление `home` доступно только аутентифицированным пользователям. Оно возвращает главную страницу приложения.

### Представления для входа и регистрации

```python
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
```

Эти функции обрабатывают запросы на вход и регистрацию пользователей.

### Представления для API

```python
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class EmployeeFloorViewSet(viewsets.ModelViewSet):
    queryset = EmployeeFloor.objects.all()
    serializer_class = EmployeeFloorSerializer

class EmployeeDayViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDay.objects.all()
    serializer_class = EmployeeDaySerializer

class ClientInfoViewSet(viewsets.ModelViewSet):
    queryset = ClientInfo.objects.all()
    serializer_class = ClientInfoSerializer
```

Класс `RoomViewSet` и подобные ему являются частью REST API, обеспечивающей CRUD-операции над моделями.

### Другие представления

```python
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

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'hotel_api/client_list.html', {'clients': clients})

def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'hotel_api/employee_list.html', {'employees': employees})

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

def days_list(request):
    days = Day.objects.all()
    return render(request, 'hotel_api/days_list.html', {'days': days})

def employee_floors_list(request):
    employee_floors = EmployeeFloor.objects.all()
    return render(request, 'hotel_api/employee_floors_list.html', {'employee_floors': employee_floors})

def employee_days_list(request):
    employee_days = EmployeeDay.objects.all()
    return render(request, 'hotel_api/employee_days_list.html', {'employee_days': employee_days})

```

Эти функции отвечают за отображение страниц со списками сущностей, таких как комнаты и клиенты.


