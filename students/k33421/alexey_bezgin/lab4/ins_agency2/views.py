from django.db.models import Count
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

# мои импорты
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login


@csrf_exempt
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def sign_in(request):
    request_json = json.loads(request.body)
    print(request_json)
    username = request_json['username']
    password = request_json['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user=user)
        return Response(status=200)
    else:
        return Response(status=404)


@csrf_exempt
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def sign_up(request):
    request_json = json.loads(request.body)
    print(request_json)
    username = request_json['username']
    password = request_json['password']
    user = User.objects.create_user(username=username, password=password)
    if user is not None:
        return Response(status=200)
    else:
        return Response(status=404)


@csrf_exempt
def get_collective_agreements(request):
    temp = CollectiveAgreement.objects.all()
    serializer = CollectiveAgreementSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_indiv_agreements(request):
    temp = IndividualAgreement.objects.all()
    serializer = IndividualAgreementSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_collective_insurance(request, pk):
    temp = CollectiveInsuranceClaim.objects.all().filter(agreement=pk)
    serializer = CollectiveInsuranceSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_indiv_insurance(request, pk):
    temp = IndividualInsuranceClaim.objects.all().filter(employee=pk)
    serializer = IndivInsuranceSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_employees(request, pk):
    temp = Employee.objects.all().filter(company=pk)
    serializer = EmployeeSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_agents(request):
    temp = Agent.objects.all()
    serializer = AgentSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_agent(request, pk):
    temp = Agent.objects.all().filter(id=pk)
    serializer = AgentSerializer(temp, many=True)
    print(serializer.data, type(serializer.data))
    return JsonResponse(serializer.data, safe=False)


from collections import OrderedDict
@csrf_exempt
def get_agent_null(request):
    temp = [OrderedDict((('id', 'Идентификатор'),('full_name', 'Полное имя'), ('passport_data', "Паспортные данные"), ('contact_details', "Контакты")))]
    print(temp, type(temp))
    return JsonResponse(temp, safe=False)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def delete_agent(request):
    request_json = json.loads(request.body)
    agent_id = request_json['id']
    Agent.objects.filter(id=agent_id).delete()
    return Response(status=200)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def create_agent(request):
    request_json = json.loads(request.body)
    print(request_json)
    agent_id = request_json['id']
    full_name = request_json['full_name']
    passport_data = request_json['passport_data']
    contact_details = request_json['contact_details']
    if Agent.objects.all().filter(id=agent_id):
        Agent.objects.filter(id=agent_id).update(full_name=full_name, passport_data=passport_data, contact_details=contact_details)
        return Response(status=200)
    else:
        Agent.objects.create(id=agent_id, full_name=full_name, passport_data=passport_data, contact_details=contact_details)
        return Response(status=200)
    return Response(status=400)


@csrf_exempt
def get_company(request, pk):
    temp = Company.objects.all().filter(id=pk)
    serializer = CompanySerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_company_null(request):
    temp = [OrderedDict((('id', 'Идентификатор'),('code', 'Полное имя'), ('full_name', "Полное название"), ('short_name', "Сокращенное название"),
        ('address', "Адрес"), ('bank_details', "Банковская информация"), ('specialization', "Сфера")))]
    print(temp, type(temp))
    return JsonResponse(temp, safe=False)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def delete_company(request):
    request_json = json.loads(request.body)
    agent_id = request_json['id']
    Company.objects.filter(id=agent_id).delete()
    return Response(status=200)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def create_company(request):
    request_json = json.loads(request.body)
    print(request_json)
    company_id = request_json['id']
    code = request_json['code']
    full_name = request_json['full_name']
    short_name = request_json['short_name']
    address = request_json['address']
    bank_details = request_json['bank_details']
    specialization = request_json['specialization']
    if Company.objects.all().filter(id=company_id):
        Company.objects.filter(id=company_id).update(full_name=full_name, short_name=short_name,
            address=address, bank_details=bank_details, specialization=specialization, code=code)
        return Response(status=200)
    else:
        Company.objects.create(id=company_id, full_name=full_name, short_name=short_name,
            address=address, bank_details=bank_details, specialization=specialization, code=code)
        return Response(status=200)
    return Response(status=400)


@csrf_exempt
def get_coll_agr(request, pk):
    temp = CollectiveAgreement.objects.all().filter(id=pk)
    serializer = CompanySerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_coll_agr_null(request):
    temp = [OrderedDict((('id', 'Идентификатор'),('code', 'Полное имя'), ('full_name', "Полное название"), ('short_name', "Сокращенное название"),
        ('address', "Адрес"), ('bank_details', "Банковская информация"), ('specialization', "Сфера")))]
    print(temp, type(temp))
    return JsonResponse(temp, safe=False)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def delete_coll_agr(request):
    request_json = json.loads(request.body)
    agent_id = request_json['id']
    CollectiveAgreement.objects.filter(id=agent_id).delete()
    return Response(status=200)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def create_coll_agr(request):
    request_json = json.loads(request.body)
    print(request_json)
    company_id = request_json['id']
    company = request_json['company']
    agent = request_json['agent']
    start_date = request_json['start_date']
    end_date = request_json['end_date']
    total_payout = request_json['total_payout']
    if Company.objects.all().filter(id=company_id):
        CollectiveAgreement.objects.filter(id=company_id).update(company=company, agent=agent,
            start_date=start_date, end_date=end_date)
        return Response(status=200)
    else:
        CollectiveAgreement.objects.create(id=company_id, company=company, agent=agent,
            start_date=start_date, end_date=end_date)
        return Response(status=200)
    return Response(status=400)


@csrf_exempt
def get_companies(request):
    temp = Company.objects.all()
    serializer = CompanySerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)


class CompanyNotExpiredAgreementsView(APIView):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)

        # Find collective agreements with the given company
        collective_agreements = CollectiveAgreement.objects.filter(company=company)

        # Get agents from these agreements
        agents = collective_agreements.values_list('agent', flat=True).distinct()

        # Extract all collective agreements with these agents
        related_agreements = CollectiveAgreement.objects.filter(agent__in=agents)

        # Find all companies that have the same agents in collective agreements
        companies_with_related_agents = Company.objects.filter(
            collectiveagreement__agent__in=related_agreements.values_list('agent', flat=True).distinct()
        ).exclude(id=company_id).distinct()

        serializer = CompanyNotExpiredAgreementsSerializer(companies_with_related_agents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# here is a trouble
class AgentAgreementsCountView(APIView):
    def get(self, request, start_date, end_date):
        # Get all collective agreements within the specified date range
        collective_agreements = CollectiveAgreement.objects.filter(
            start_date__gte=start_date,
            start_date__lte=end_date
        )

        # Group them by agents and count
        collective_counts = collective_agreements.values('agent').annotate(collective_count=Count('agent'))

        # Get all individual agreements within the specified date range
        individual_agreements = IndividualAgreement.objects.filter(
            start_date__gte=start_date,
            start_date__lte=end_date
        )

        # Group them by agents and count
        individual_counts = individual_agreements.values('agent').annotate(individual_count=Count('agent'))

        # Merge the counts for each agent
        agent_counts = {}
        for collective_count in collective_counts:
            agent_id = collective_count['agent']
            agent_counts.setdefault(agent_id, {}).update({'collective_count': collective_count['collective_count']})

        for individual_count in individual_counts:
            agent_id = individual_count['agent']
            agent_counts.setdefault(agent_id, {}).update({'individual_count': individual_count['individual_count']})

        # Get agent names
        agent_names = Agent.objects.filter(id__in=agent_counts.keys()).values('id', 'full_name')

        # Final result in the desired format
        result = [
            {
                "agent_name": agent['full_name'],
                "collective_count": agent_counts[agent['id']].get('collective_count', 0),
                "individual_count": agent_counts[agent['id']].get('individual_count', 0),
            }
            for agent in agent_names
        ]

        serializer = AgentAgreementsCountSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 3 функция -- странно
# согласно моей модели данных это выглядит странно
# человек работает строго в 1 компании (бессрочный рабский контракт)
class EmployeesInSameCompanyView(APIView):
    def get(self, request, employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)

        # Get the company of the given employee
        employee_company = employee.company

        # Get all other employees in the same company
        other_employees = Employee.objects.filter(company=employee_company).exclude(id=employee_id).distinct()

        serializer = UniqueEmployeesInCollectiveAgreementsSerializer(other_employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PayoutSummaryView(APIView):
    def get(self, request, start_date, end_date):
        collective_payout = CollectiveInsuranceClaim.objects.filter(
            date_of_claim__gte=start_date, date_of_claim__lte=end_date
        ).aggregate(Sum('payout_amount'))['payout_amount__sum'] or 0

        individual_payout = IndividualInsuranceClaim.objects.filter(
            date_of_claim__gte=start_date, date_of_claim__lte=end_date
        ).aggregate(Sum('payout_amount'))['payout_amount__sum'] or 0

        serializer = PayoutSummarySerializer({
            'collective_payout': collective_payout,
            'individual_payout': individual_payout,
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyPayoutSummaryView(APIView):
    def get(self, request):
        companies = Company.objects.all()

        company_data = []
        for company in companies:
            company_employees = Employee.objects.filter(company=company)
            company_employees_cats = list(company_employees.values_list('risk_category', flat=True))

            # счетчики по категориям
            total_payout_first = 0
            total_payout_second = 0
            total_payout_third = 0

            # считаем, что если collective, то выплачиваем каждому
            # в collective все-все сотрудники, так что считаем общую сумму и умножаем на частоты категорий
            total_payout_collective = CollectiveInsuranceClaim.objects.filter(
                agreement__company=company).aggregate(Sum('payout_amount'))['payout_amount__sum'] or 0

            total_payout_first += total_payout_collective * company_employees_cats.count('first')
            total_payout_second += total_payout_collective * company_employees_cats.count('second')
            total_payout_third += total_payout_collective * company_employees_cats.count('third')

            # добавляем individual. в таком случае прибавляем то только одному
            for employee, employee_cat in zip(company_employees, company_employees_cats):
                employee_individual_claims = IndividualInsuranceClaim.objects.filter(
                    employee_id=employee.id
                ).aggregate(Sum('payout_amount'))['payout_amount__sum'] or 0

                if employee_cat == 'first':
                    total_payout_first += employee_individual_claims
                elif employee_cat == 'second':
                    total_payout_second += employee_individual_claims
                else:
                    total_payout_third += employee_individual_claims

            company_serializer_data = {
                'bank_details': company.bank_details,
                'total_payout_first_category': total_payout_first,
                'total_payout_second_category': total_payout_second,
                'total_payout_third_category': total_payout_third,
            }

            company_data.append(company_serializer_data)

        serializer = CompanyPayoutSummarySerializer(company_data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ReportView(APIView):
    def get(self, request):
        agents = Agent.objects.all()

        agent_data = []
        for agent in agents:
            agent_collective_agreements = CollectiveAgreement.objects.filter(
                start_date__lte=timezone.localtime(), end_date__gte=timezone.localtime(),
                agent=agent
            )
            agent_individual_agreements = IndividualAgreement.objects.filter(
                start_date__lte=timezone.localtime(), end_date__gte=timezone.localtime(),
                agent=agent
            )

            agent_collective_payout = agent_collective_agreements.aggregate(Sum('total_payout'))[
                                          'total_payout__sum'] or 0
            agent_individual_payout = agent_individual_agreements.aggregate(Sum('total_payout'))[
                                          'total_payout__sum'] or 0

            agent_collective_claims = CollectiveInsuranceClaim.objects.filter(
                agreement__agent=agent
            )

            agent_individual_claims = IndividualInsuranceClaim.objects.filter(
                employee__agent=agent
            )

            agent_collective_payout_claims = agent_collective_claims.aggregate(Sum('payout_amount'))[
                                                 'payout_amount__sum'] or 0
            agent_individual_payout_claims = agent_individual_claims.aggregate(Sum('payout_amount'))[
                                                 'payout_amount__sum'] or 0

            agent_serializer_data = {
                'agent_id': agent.id,
                'agent_full_name': agent.full_name,
                'total_collective_agreements': agent_collective_agreements.count(),
                'total_collective_payout': agent_collective_payout,
                'total_individual_agreements': agent_individual_agreements.count(),
                'total_individual_payout': agent_individual_payout,
                "total_collective_claims": agent_collective_claims.count(),
                "total_collective_payout_claims": agent_collective_payout_claims,
                "total_individual_claims": agent_individual_claims.count(),
                "total_individual_payout_claims": agent_individual_payout_claims,
            }

            agent_data.append(agent_serializer_data)

        company_data = []
        companies = Company.objects.all()

        for company in companies:
            company_collective_agreements = CollectiveAgreement.objects.filter(company=company)
            company_collective_count = company_collective_agreements.count()
            company_collective_payout = company_collective_agreements.aggregate(Sum('total_payout'))[
                                            'total_payout__sum'] or 0

            company_collective_claims = CollectiveInsuranceClaim.objects.filter(agreement__company=company)
            company_collective_claims_count = company_collective_claims.count()
            company_collective_claims_payout = company_collective_claims.aggregate(Sum('payout_amount'))[
                                                   'payout_amount__sum'] or 0

            company_employees = Employee.objects.filter(company=company)
            company_individual_count = 0
            company_individual_payout = 0

            company_individual_claims_count = 0
            company_individual_claims_payout = 0

            for employee in company_employees:
                employee_individual_agreements = IndividualAgreement.objects.filter(
                    employee_id=employee.id
                )

                company_individual_count += employee_individual_agreements.count()
                company_individual_payout += employee_individual_agreements.aggregate(Sum('total_payout'))[
                                                 'total_payout__sum'] or 0

                employee_individual_claims = IndividualInsuranceClaim.objects.filter(
                    employee_id=employee.id
                )

                company_individual_claims_count += employee_individual_claims.count()
                company_individual_claims_payout += employee_individual_claims.aggregate(Sum('payout_amount'))[
                                                        'payout_amount__sum'] or 0

            company_serializer_data = {
                'company_id': company.id,
                'company_full_name': company.full_name,
                'total_collective_agreements': company_collective_count,
                'total_collective_payout': company_collective_payout,
                'total_individual_agreements': company_individual_count,
                'total_individual_payout': company_individual_payout,
                "total_collective_claims": company_collective_claims_count,
                "total_collective_payout_claims": company_collective_claims_payout,
                "total_individual_claims": company_individual_claims_count,
                "total_individual_payout_claims": company_individual_claims_payout,
            }
            company_data.append(company_serializer_data)

        agent_serializer = AgentReportSerializer(agent_data, many=True)
        company_serializer = CompanyReportSerializer(company_data, many=True)

        return Response({
            'agent_report': agent_serializer.data,
            'company_report': company_serializer.data

        }, status=status.HTTP_200_OK)


class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class AgentCreateView(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class AgentContractCreateView(generics.CreateAPIView):
    queryset = AgentContract.objects.all()
    serializer_class = AgentContractSerializer


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CollectiveAgreementCreateView(generics.CreateAPIView):
    queryset = CollectiveAgreement.objects.all()
    serializer_class = CollectiveAgreementSerializer


class IndividualAgreementCreateView(generics.CreateAPIView):
    queryset = IndividualAgreement.objects.all()
    serializer_class = IndividualAgreementSerializer


class CollectiveInsuranceClaimCreateView(generics.CreateAPIView):
    queryset = CollectiveInsuranceClaim.objects.all()
    serializer_class = CollectiveInsuranceClaimSerializer


class IndividualInsuranceClaimCreateView(generics.CreateAPIView):
    queryset = IndividualInsuranceClaim.objects.all()
    serializer_class = IndividualInsuranceClaimSerializer
