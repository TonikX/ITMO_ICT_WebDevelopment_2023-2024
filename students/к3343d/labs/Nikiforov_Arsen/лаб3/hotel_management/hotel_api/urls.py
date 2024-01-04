from django import views
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import (
    RoomViewSet, ClientViewSet, EmployeeViewSet, FloorViewSet,
    FloorOccupancyViewSet, DayViewSet, EmployeeFloorViewSet,
    EmployeeDayViewSet, ClientInfoViewSet, ComplexRoomViewSet,
    NestedClientViewSet, UserViewSet, BookingViewSet,update_room_status,
    RoomStatisticsView, home, register_view,
    login_view, alternative_login_view, api_login,
    generate_token, register_user, book_room,
    rooms_list, clients_list, employees_list, floors_list,
    client_info_list, days_list, employee_floors_list,
    employee_days_list, bookings_list, book_selected_rooms
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from .views import ReviewViewSet
from . import views

app_name = 'hotel_api'

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API description",
    
    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'floors', FloorViewSet)
router.register(r'days', DayViewSet)
router.register(r'employee_floors', EmployeeFloorViewSet)
router.register(r'employee_days', EmployeeDayViewSet)
router.register(r'client_info', ClientInfoViewSet)
router.register(r'complex_rooms', ComplexRoomViewSet)
router.register(r'nested_clients', NestedClientViewSet)
router.register(r'floor_occupancy', FloorOccupancyViewSet)
router.register(r'users', UserViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('rooms/', rooms_list, name='rooms_list'),
    path('book_selected_rooms/', book_selected_rooms, name='book_selected_rooms'),
    path('register/', register_user, name='register_user'),
    path('login/', login_view, name='login'),
    path('alternative_login/', alternative_login_view, name='alternative_login'),
    path('register/', register_view, name='register'),
    path('clients/', clients_list, name='clients_list'),
    path('employees/', employees_list, name='employees_list'),
    path('floors/', floors_list, name='floors_list'),
    path('client-info/', client_info_list, name='client_info_list'),
    path('days/', days_list, name='days_list'),
    path('employee-floors/', employee_floors_list, name='employee_floors_list'),
    path('employee-days/', employee_days_list, name='employee_days_list'),
    path('bookings/', bookings_list, name='bookings_list'),
    path('api/login/', api_login, name='api_login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/rooms/<int:room_id>/book_room/', views.book_room, name='book_room'),
    path('api/room-statistics/', RoomStatisticsView.as_view(), name='room-statistics'),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/rooms/<int:room_id>/check_in', update_room_status, name='update_room_status'),
    path('api/bookings/<int:pk>/confirm/', BookingViewSet.as_view({'post': 'confirm_booking'}), name='confirm-booking'),
    path('api/bookings/<int:pk>/cancel/', BookingViewSet.as_view({'post': 'cancel_booking'}), name='cancel-booking'),
    
]
