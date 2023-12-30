# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Room, Client, Employee, Floor, Day, EmployeeFloor, EmployeeDay, ClientInfo, Booking, CustomUser
from .serializers import (RoomSerializer, ClientSerializer, EmployeeSerializer, 
                          FloorSerializer, DaySerializer, EmployeeFloorSerializer, 
                          EmployeeDaySerializer, ClientInfoSerializer, BookingSerializer, 
                          ComplexRoomSerializer, NestedClientSerializer, FloorOccupancySerializer, 
                          UserSerializer)
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from datetime import datetime
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, TokenError
import json
from rest_framework.views import APIView
from django.db.models import Count, Avg

User = get_user_model()

class RoomStatisticsView(APIView):
    def get(self, request, format=None):
        stats = Room.objects.values('room_type').annotate(
            total=Count('id'),
            average_cost=Avg('cost')
        ).order_by('room_type')
        return Response(stats)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class FloorOccupancyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorOccupancySerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=False, methods=['get'])
    def by_date(self, request):
        date = request.query_params.get('date')
        bookings = Booking.objects.filter(start_date=date)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

class ComplexRoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.filter(status='occupied').prefetch_related('clients', 'employee_floor_set')
    serializer_class = ComplexRoomSerializer

class NestedClientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.select_related('room', 'client_info')
    serializer_class = NestedClientSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

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

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            try:
                AccessToken(access_token)
                login(request, user)
                return JsonResponse({'status': 'success', 'refresh': str(refresh), 'access': access_token})
            except TokenError as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=401)
        else:
            return JsonResponse({'status': 'error'}, status=401)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if room.status != 'available':
        return JsonResponse({'status': 'error', 'message': 'Room is not available'}, status=400)
    start_date = request.data.get('start_date')
    end_date = request.data.get('end_date')
    if not start_date or not end_date:
        return JsonResponse({'status': 'error', 'message': 'Start date and end date are required'}, status=400)
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        if start_date >= end_date:
            return JsonResponse({'status': 'error', 'message': 'End date must be after start date'}, status=400)
    except ValueError:
        return JsonResponse({'status': 'error', 'message': 'Invalid date format'}, status=400)
    booking = Booking.objects.create(user=request.user, room=room, start_date=start_date, end_date=end_date)
    room.status = 'booked'
    room.save()
    return JsonResponse({'status': 'success', 'booking_id': booking.id})

def rooms_list(request):
    room_type_query = request.GET.get('room_type', '').strip()
    room_status_query = request.GET.get('room_status', '').strip()
    rooms = Room.objects.all()
    if room_type_query:
        rooms = rooms.filter(room_type__iexact=room_type_query)
    if room_status_query:
        rooms = rooms.filter(status__iexact=room_status_query)
    return render(request, 'hotel_api/rooms_list.html', {'rooms': rooms})

@login_required
def book_selected_rooms(request):
    if request.method == 'POST':
        room_ids = request.POST.getlist('room_ids')
        rooms = Room.objects.filter(id__in=room_ids, is_available=True)
        for room in rooms:
            room.booked_by = request.user
            room.is_available = False
            room.save()
        return redirect('rooms_list')
    return render(request, 'hotel_api/rooms_list.html')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_token(request):
    user = request.user
    refresh = RefreshToken.for_user(user)
    refresh.access_token.set_exp(timezone.now() + SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'])
    access_token = str(refresh.access_token)
    return Response({'access_token': access_token})

@csrf_exempt
def api_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({'refresh': str(refresh), 'access': str(refresh.access_token)})
        else:
            return JsonResponse({'message': 'Неверные учетные данные'}, status=401)
    return JsonResponse({'message': 'Неверный запрос'}, status=400)

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
        return JsonResponse({'id': user.id, 'username': user.username}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def login_redirect(request):
    return redirect("http://localhost:8080/login")

def alternative_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("с днем рождения!")
            pass
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='/login/')
def home(request):
    return render(request, 'hotel_api/home.html')

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

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'hotel_api/client_list.html', {'clients': clients})

def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'hotel_api/employee_list.html', {'employees': employees})

def bookings_list(request):
    return render(request, 'hotel_api/bookings_list.html')

def floors_list(request):
    floors = Floor.objects.all()
    return render(request, 'hotel_api/floor_list.html', {'floors': floors})

def staff_management(request):
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
