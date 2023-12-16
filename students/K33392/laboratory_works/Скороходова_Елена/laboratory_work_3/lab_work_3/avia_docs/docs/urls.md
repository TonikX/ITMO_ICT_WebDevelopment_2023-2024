##Urls

Я использую роутеры для автоматической генерации Url-маршрутов для каждого ViewSet,
a также добавляю явные URL-маршруты для детализированных представлений и других необходимых эндпоинтов (токены, регистрация)

routers.DefaultRouter():

Создается объект DefaultRouter из библиотеки Django REST Framework. 
DefaultRouter автоматически создает URL-маршруты для предоставленных 
представлений ViewSet.

Регистрация представлений с помощью router.register:

Каждый ViewSet регистрируется в роутере с указанием пути ('airplanes', 'flights', и так далее) и соответствующего представления.

urlpatterns:

Создается список URL-маршрутов.
Для каждой модели (Airplane, Flight, CrewMember, TransitStop, Employee) определены URL-маршруты для отдельного представления с использованием path.
Токены (create и destroy) и регистрация пользователя также имеют свои URL-маршруты.

urlpatterns += router.urls:

URL-маршруты, созданные роутером, добавляются к основному списку URL-маршрутов. 
Это включает URL-маршруты, соответствующие 
ViewSet для airplanes, flights, и так далее.

    from django.urls import path
    from rest_framework import routers
    from djoser.views import TokenCreateView, TokenDestroyView
    from .views import (
        AirplaneDetailView, FlightDetailView,
        CrewMemberDetailView, TransitStopDetailView,
        EmployeeDetailView, UserCreateView, AirplaneViewSet, FlightViewSet, CrewMemberViewSet, TransitStopViewSet,
        EmployeeViewSet
    )
    
    
    router = routers.DefaultRouter()
    
    
    router.register(r'airplanes', AirplaneViewSet, basename='airplane')
    router.register(r'flights', FlightViewSet, basename='flight')
    router.register(r'crewmembers', CrewMemberViewSet, basename='crewmember')
    router.register(r'transitstops', TransitStopViewSet, basename='transitstop')
    router.register(r'employees', EmployeeViewSet, basename='employee')
    
    
    urlpatterns = [
        path('airplanes/<int:pk>/', AirplaneDetailView.as_view(), name='airplane-detail'),
        path('flights/<int:pk>/', FlightDetailView.as_view(), name='flight-detail'),
        path('crewmembers/<int:pk>/', CrewMemberDetailView.as_view(), name='crewmember-detail'),
        path('transitstops/<int:pk>/', TransitStopDetailView.as_view(), name='transitstop-detail'),
        path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
        path('token/create/', TokenCreateView.as_view(), name='token-create'),
        path('token/destroy/', TokenDestroyView.as_view(), name='token-destroy'),
        path('register/', UserCreateView.as_view(), name='user-register'),
    ]
    
    urlpatterns += router.urls
