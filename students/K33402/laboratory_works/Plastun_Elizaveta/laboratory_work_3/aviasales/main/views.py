from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from django.db.models import Count

from .models import *
from .serializers import *


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# Airline Company Views
class AirlineCompanyListView(generics.ListAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]


class AirlineCompanyRetrieveView(generics.RetrieveAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]


class AirlineCompanyCreateView(generics.CreateAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
    permission_classes = [permissions.IsAuthenticated, ]


class AirlineCompanyUpdateView(generics.UpdateAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
    permission_classes = [permissions.IsAuthenticated, ]


class AirlineCompanyDeleteView(generics.DestroyAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
    permission_classes = [permissions.IsAuthenticated, ]


# Airplane Views
class AirplaneListView(generics.ListAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]


class AirplaneRetrieveView(generics.RetrieveAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]


class AirplaneCreateView(generics.CreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [permissions.IsAuthenticated]


class AirplaneUpdateView(generics.UpdateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [permissions.IsAuthenticated]


class AirplaneDeleteView(generics.DestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [permissions.IsAuthenticated]


# Crew Views
class CrewListView(generics.ListAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CrewRetrieveView(generics.RetrieveAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CrewCreateView(generics.CreateAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticated]


class CrewUpdateView(generics.UpdateAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticated]


class CrewDeleteView(generics.DestroyAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticated]


# Crew Member Views
class CrewMemberListView(generics.ListAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CrewMemberRetrieveView(generics.RetrieveAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CrewMemberCreateView(generics.CreateAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class CrewMemberUpdateView(generics.UpdateAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class CrewMemberDeleteView(generics.DestroyAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


# Route Views
class RouteListView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RouteRetrieveView(generics.RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RouteCreateView(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]


class RouteUpdateView(generics.UpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]


class RouteDeleteView(generics.DestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]


# Flight Views
class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FlightRetrieveView(generics.RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FlightCreateView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticated]


class FlightUpdateView(generics.UpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticated]


class FlightDeleteView(generics.DestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticated]


class MostFrequentAirplaneBrand(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, route_id):
        most_frequent_airplane = Flight.objects.filter(route_id=route_id).values('airplanes__plane_type') \
            .annotate(count=Count('airplanes')).order_by('-count').first()

        if most_frequent_airplane:
            most_frequent_brand = most_frequent_airplane['airplanes__plane_type']
            return Response({'most_frequent_brand': most_frequent_brand})
        else:
            return Response({'most_frequent_brand': None})


class RoutesBelowCapacity(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, percentage):
        threshold = (100 - float(percentage)) / 100
        under_capacity_routes = Route.objects.annotate(
            average_capacity=Count('flights__sold_tickets') / Count('flights')
        ).filter(average_capacity__lt=threshold)
        serializer = RouteSerializer(under_capacity_routes, many=True)
        return Response({'under_capacity_routes': serializer.data})


class AvailableSeats(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, flight_id):
        try:
            flight = Flight.objects.get(pk=flight_id)
        except Flight.DoesNotExist:
            return Response({'error': 'Flight not found'}, status=status.HTTP_404_NOT_FOUND)

        available_seats = flight.airplanes.first().seats_capacity - flight.sold_tickets
        return Response({'available_seats': available_seats})


class AirplanesUnderRepair(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        under_repair_count = Airplane.objects.filter(under_repair=True).count()
        return Response({'airplanes_under_repair': under_repair_count})


class TotalEmployees(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, company_id):
        try:
            company = AirlineCompany.objects.get(pk=company_id)
        except AirlineCompany.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

        total_employees = CrewMember.objects.filter(company=company).count()
        return Response({'total_employees': total_employees})
