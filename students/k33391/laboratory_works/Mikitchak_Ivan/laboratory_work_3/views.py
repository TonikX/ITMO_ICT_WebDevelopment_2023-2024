from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.db.models import Sum
from django.utils import timezone


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class NaturalPersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NaturalPerson.objects.all()
    serializer_class = NaturalPersonSerializer

class SpecializationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NaturalPerson.objects.all()
    serializer_class = NaturalPersonSerializer

class LegalPersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer

class NaturalPersonContractViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NaturalPersonContract.objects.all()
    serializer_class = LegalPersonSerializer
    
class LegalPersonContractViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LegalPersonContract.objects.all()
    serializer_class = LegalPersonSerializer
    
class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class InsuredEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InsuredEvent.objects.all()
    serializer_class = InsuredEventSerializer

class SameAgentsLegalPersonsAPIView(APIView):
    def get(self, request, pk):
        try:
            legal_person = LegalPerson.objects.get(pk=pk)
        except LegalPerson.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        today_date = timezone.now().date()
        active_contracts = LegalPersonContract.objects.filter(till__gt=today_date)
        
        my_active_contracts = active_contracts.filter(legal_person=legal_person)
        my_agents = set()
        for contract in my_active_contracts:
            my_agents.add(contract.agent)
        
        same_agents_active_contracts = active_contracts.exclude(legal_person=legal_person.id).filter(agent__in=my_agents)
        same_agents_legal_persons = []
        for contract in same_agents_active_contracts:
            same_agents_legal_persons.append(contract.legal_person)
        
        serializer = LegalPersonSerializer(same_agents_legal_persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        

class AgentContractsStatsAPIView(APIView):
    def get(self, request, pk):
        since = request.data.get('since')
        till = request.data.get('till')
        try:
            agent = Agent.objects.get(pk=pk)
        except Agent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        natural_count = agent.naturalpersoncontract_set.filter(since__gte=since, since__lte=till).count()
        legal_count = agent.legalpersoncontract_set.filter(since__gte=since, since__lte=till).count()
        
        contracts_data = {
            "natural_person_contracts_count": natural_count,
            "legal_person_contracts_count": legal_count
        }

        return Response(contracts_data, status=status.HTTP_200_OK)

class InsuredColleaguesAPIView(APIView):
    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        queryset = Employee.objects.filter(contract=employee.contract)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class InsuredEventsTimeframeAPIView(APIView):
    def get(self, request):
        since = request.data.get('since')
        till = request.data.get('till')
        queryset = InsuredEvent.objects.filter(date__gte=since, date__lte=till)
        natural_contracts_payments = queryset.filter(contract_type='natural_person').aggregate(natural_sum=Sum('payment'))['natural_sum']
        legal_contracts_payments = queryset.filter(contract_type='legal_person').aggregate(legal_sum=Sum('payment'))['legal_sum']
        
        payments_data = {
            "natural_contracts_payments": natural_contracts_payments,
            "legal_contracts_payments": legal_contracts_payments
        }

        return Response(payments_data, status=status.HTTP_200_OK)
    
class LegalPersonsAndContractsAPIView(APIView):
    def get(self, request):
        queryset = LegalPerson.objects.all()
        serializer = LegalPersonAndContractSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReportAPIView(APIView):
    def get(self, request):
        report_data = []
        today_date = timezone.now().date()        
        for agent in Agent.objects.all():
            natural_queryset = agent.naturalpersoncontract_set.filter(till__gt=today_date)
            natural_count = natural_queryset.count()
            natural_sums = natural_queryset.aggregate(natural_premium_sum=Sum('premium'),
                                                      natural_payment_sum=Sum('payment'))
            
            legal_queryset = agent.legalpersoncontract_set.filter(till__gt=today_date)
            legal_count = legal_queryset.count()
            legal_sums = legal_queryset.aggregate(
                legal_low_premium_sum=Sum('low_premium'),
                legal_medium_premium_sum=Sum('medium_premium'),
                legal_high_premium_sum=Sum('high_premium'),
                legal_low_payment_sum=Sum('low_payment'),
                legal_medium_payment_sum=Sum('medium_payment'),
                legal_high_payment_sum=Sum('high_payment')
            )
            
            agent_data = {
                'id': agent.id,
                'full_name': agent.full_name,
                'natural_contracts_count': natural_count,
                'natural_contracts_premium': natural_sums['natural_premium_sum'],
                'natural_contracts_payment': natural_sums['natural_payment_sum'],
                'legal_contracts_count': legal_count,
                'legal_contracts_low_premium': legal_sums['legal_low_premium_sum'],
                'legal_contracts_medium_premium': legal_sums['legal_medium_premium_sum'],
                'legal_contracts_high_premium': legal_sums['legal_high_premium_sum'],
                'legal_contracts_low_payment': legal_sums['legal_low_payment_sum'],
                'legal_contracts_medium_payment': legal_sums['legal_medium_payment_sum'],
                'legal_contracts_high_payment': legal_sums['legal_high_payment_sum']
            }
            report_data.append(agent_data)
            
        return Response(report_data, status=status.HTTP_200_OK)
