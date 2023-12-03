### Компания авиаперевозчик

#### `airline_companies/all/`

Получение список всех авиакомпаний

```
class AirlineCompanyListView(generics.ListAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]
```

#### `airline_companies/<int:pk>/`

Получение информации о конкретной компании

```
class AirlineCompanyRetrieveView(generics.RetrieveAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]
```

#### `airline_companies/new/`

Создание нового экземпляра модели

```
class AirlineCompanyCreateView(generics.CreateAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
    permission_classes = [permissions.IsAuthenticated,]
```

#### `airline_companies/update/<int:pk>/`

Изменение модели

```
class AirlineCompanyUpdateView(generics.UpdateAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
    permission_classes = [permissions.IsAuthenticated,]
```

### Самолет

#### `airplanes/all/`

Получение список всех самолетах

```
class AirplaneListView(generics.ListAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]
```

#### `airplanes/<int:pk>/`

Получение информации о конкретном самолете

```
class AirplaneRetrieveView(generics.RetrieveAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]
```

#### `airplanes/new/`

Создание нового экземпляра модели

```
class AirplaneCreateView(generics.CreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [permissions.IsAuthenticated]
```

#### `airplanes/update/<int:pk>/`

Изменение модели

```
class AirplaneUpdateView(generics.UpdateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [permissions.IsAuthenticated]
```

### Экипаж

#### `crews/all/`

Получение список всех экипажах

```
class CrewListView(generics.ListAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

#### `crews/<int:pk>/`

Получение информации о конкретном экипаже

```
class CrewRetrieveView(generics.RetrieveAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

#### `crews/new/`

Создание нового экземпляра модели

```
class CrewCreateView(generics.CreateAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticated]
```

#### `crews/update/<int:pk>/`

Изменение модели

```
class CrewUpdateView(generics.UpdateAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticated]
```

### Сотрудник

#### `crew_members/all/`

Получение список всех сотрудников

```
class CrewMemberListView(generics.ListAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

#### `crew_members/<int:pk>/`

Получение информации о конкретном сотруднике

```
class CrewMemberRetrieveView(generics.RetrieveAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

#### `crew_members/new/`

Создание нового экземпляра модели

```
class CrewMemberCreateView(generics.CreateAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [permissions.IsAuthenticated]
```

#### `crew_members/update/<int:pk>/`

Изменение модели

```
class CrewMemberUpdateView(generics.UpdateAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [permissions.IsAuthenticated]
```

### Маршрут

#### `routes/all/`

Получение список всех маршрутов

```
class RouteListView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

#### `routes/<int:pk>/`

Получение информации о конкретном маршруте

```
class RouteRetrieveView(generics.RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

#### `routes/new/`

Создание нового экземпляра модели

```
class RouteCreateView(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]
```

#### `routes/update/<int:pk>/`

Изменение модели

```
class RouteUpdateView(generics.UpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]
```

### Рейс

#### `flights/all/`

Получение список всех полетов

```
class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

#### `flights/<int:pk>/`

Получение информации о конкретном полете

```
class FlightRetrieveView(generics.RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

```

#### `flights/new/`

Создание нового экземпляра модели

```
class FlightCreateView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticated]
```

#### `flights/update/<int:pk>/`

Изменение модели

```
class FlightUpdateView(generics.UpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticated]
```

### Дополнительные методы

#### `most_frequent_airplane_brand/<int:route_id>/`

Выбрать марку самолета, которая чаще всего летает по маршруту.

```
class MostFrequentAirplaneBrand(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, route_id):
        most_frequent_airplane = Flight.objects.filter(route_id=route_id).values('airplanes__plane_type')\
            .annotate(count=Count('airplanes')).order_by('-count').first()

        if most_frequent_airplane:
            most_frequent_brand = most_frequent_airplane['airplanes__plane_type']
            return Response({'most_frequent_brand': most_frequent_brand})
        else:
            return Response({'most_frequent_brand': None})
```

#### `routes_below_capacity/<str:percentage>/`

Выбрать маршрут/маршруты, по которым летают рейсы, заполненные менее чем на ХХ %.

```
class RoutesBelowCapacity(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, percentage):
        threshold = (100 - float(percentage)) / 100
        under_capacity_routes = Route.objects.annotate(
            average_capacity=Count('flights__sold_tickets') / Count('flights')
        ).filter(average_capacity__lt=threshold)
        serializer = RouteSerializer(under_capacity_routes, many=True)
        return Response({'under_capacity_routes': serializer.data})
```

#### `available_seats/<int:flight_id>/`

Определить наличие свободных мест на заданный рейс.

```
class AvailableSeats(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, flight_id):
        try:
            flight = Flight.objects.get(pk=flight_id)
        except Flight.DoesNotExist:
            return Response({'error': 'Flight not found'}, status=status.HTTP_404_NOT_FOUND)

        available_seats = flight.airplanes.first().seats_capacity - flight.sold_tickets
        return Response({'available_seats': available_seats})
```

#### `airplanes_under_repair/`

Определить количество самолетов, находящихся в ремонте.

```
class AirplanesUnderRepair(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        under_repair_count = Airplane.objects.filter(under_repair=True).count()
        return Response({'airplanes_under_repair': under_repair_count})
```

#### `total_employees/<int:company_id>/`

Определить количество работников компания-авиаперевозчика.

```
class TotalEmployees(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, company_id):
        try:
            company = AirlineCompany.objects.get(pk=company_id)
        except AirlineCompany.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

        total_employees = CrewMember.objects.filter(company=company).count()
        return Response({'total_employees': total_employees})
```
