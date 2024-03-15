from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
    path('logout', Logout.as_view()),

    path('airline_companies/all/', AirlineCompanyListView.as_view(), name='airline_company_list'),
    path('airline_companies/<int:pk>/', AirlineCompanyRetrieveView.as_view(), name='airline_company_detail'),
    path('airline_companies/new/', AirlineCompanyCreateView.as_view(), name='airline_company_create'),
    path('airline_companies/update/<int:pk>/', AirlineCompanyUpdateView.as_view(), name='airline_company_update'),
    path('airline_companies/delete/<int:pk>/', AirlineCompanyDeleteView.as_view(), name='airline_company_delete'),

    path('airplanes/all/', AirplaneListView.as_view(), name='airplane_list'),
    path('airplanes/<int:pk>/', AirplaneRetrieveView.as_view(), name='airplane_detail'),
    path('airplanes/new/', AirplaneCreateView.as_view(), name='airplane_create'),
    path('airplanes/update/<int:pk>/', AirplaneUpdateView.as_view(), name='airplane_update'),
    path('airplanes/delete/<int:pk>/', AirplaneDeleteView.as_view(), name='airplane_delete'),

    path('crews/all/', CrewListView.as_view(), name='crew_list'),
    path('crews/<int:pk>/', CrewRetrieveView.as_view(), name='crew_detail'),
    path('crews/new/', CrewCreateView.as_view(), name='crew_create'),
    path('crews/update/<int:pk>/', CrewUpdateView.as_view(), name='crew_update'),
    path('crews/delete/<int:pk>/', CrewDeleteView.as_view(), name='crew_delete'),

    path('crew_members/all/', CrewMemberListView.as_view(), name='crew_member_list'),
    path('crew_members/<int:pk>/', CrewMemberRetrieveView.as_view(), name='crew_member_detail'),
    path('crew_members/new/', CrewMemberCreateView.as_view(), name='crew_member_create'),
    path('crew_members/update/<int:pk>/', CrewMemberUpdateView.as_view(), name='crew_member_update'),
    path('delete/update/<int:pk>/', CrewMemberDeleteView.as_view(), name='crew_member_delete'),

    path('routes/all/', RouteListView.as_view(), name='route_list'),
    path('routes/<int:pk>/', RouteRetrieveView.as_view(), name='route_detail'),
    path('routes/new/', RouteCreateView.as_view(), name='route_create'),
    path('routes/update/<int:pk>/', RouteUpdateView.as_view(), name='route_update'),
    path('routes/delete/<int:pk>/', RouteDeleteView.as_view(), name='route_delete'),

    path('flights/all/', FlightListView.as_view(), name='flight_list'),
    path('flights/<int:pk>/', FlightRetrieveView.as_view(), name='flight_detail'),
    path('flights/new/', FlightCreateView.as_view(), name='flight_create'),
    path('flights/update/<int:pk>/', FlightUpdateView.as_view(), name='flight_update'),
    path('flights/delete/<int:pk>/', FlightDeleteView.as_view(), name='flight_delete'),

    # Выбрать марку самолета, которая чаще всего летает по маршруту.
    path('most_frequent_airplane_brand/<int:route_id>/', MostFrequentAirplaneBrand.as_view(), name='most_frequent_airplane_brand'),

    # Выбрать маршрут/маршруты, по которым летают рейсы, заполненные менее чем на ХХ %.
    path('routes_below_capacity/<str:percentage>/', RoutesBelowCapacity.as_view(), name='routes_below_capacity'),

    # Определить наличие свободных мест на заданный рейс.
    path('available_seats/<int:flight_id>/', AvailableSeats.as_view(), name='available_seats'),

    # Определить количество самолетов, находящихся в ремонте.
    path('airplanes_under_repair/', AirplanesUnderRepair.as_view(), name='airplanes_under_repair'),

    # Определить количество работников компания-авиаперевозчика.
    path('total_employees/<int:company_id>/', TotalEmployees.as_view(), name='total_employees'),
]
