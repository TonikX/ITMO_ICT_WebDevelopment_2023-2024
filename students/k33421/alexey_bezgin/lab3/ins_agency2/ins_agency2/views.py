from django.db.models import Count
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


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
