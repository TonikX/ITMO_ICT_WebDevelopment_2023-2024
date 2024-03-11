"""
URL configuration for ins_agency2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('same_agreement/<int:company_id>/', CompanyNotExpiredAgreementsView.as_view(),
         name='not_expired_agreements'),
    path('agents_stat/<str:start_date>/<str:end_date>/', AgentAgreementsCountView.as_view(),
         name='counter_by_agent'),
    path('collective_agreements/<int:employee_id>/',
         EmployeesInSameCompanyView.as_view(), name='unique_employees_in_collective_agreements'),
    path('payout_summary/<str:start_date>/<str:end_date>/', PayoutSummaryView.as_view(), name='payout_summary'),
    path('companies_payouts/', CompanyPayoutSummaryView.as_view(), name='payout_summary'),
    path('report/', ReportView.as_view(), name='report'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('company/create/', CompanyCreateView.as_view(), name='company-create'),
    # path('agent/create/', AgentCreateView.as_view(), name='agent-create'),
    path('agent_contract/create/', AgentContractCreateView.as_view(), name='agent_contract-create'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('collective_agreement/create/', CollectiveAgreementCreateView.as_view(), name='collective_agreement-create'),
    path('individual_agreement/create/', IndividualAgreementCreateView.as_view(), name='individual_agreement-create'),
    path('collective_insurance_claim/create/', CollectiveInsuranceClaimCreateView.as_view(),
         name='collective_insurance_claim-create'),
    path('individual_insurance_claim/create/', IndividualInsuranceClaimCreateView.as_view(),
         name='individual_insurance_claim-create'),

    path('login/', sign_in),
    path('register/', sign_up),
    path('col-agr/', get_collective_agreements),
    path('ind-agr/', get_indiv_agreements),
    path('col-ins/<int:pk>', get_collective_insurance),
    path('ind-ins/<int:pk>', get_indiv_insurance),
    path('empl/<int:pk>', get_employees),
    path('agents/', get_agents),
    path('companies/', get_companies),

    path('agent/<int:pk>', get_agent),
    path('agent/create', get_agent_null),
    path('agent-trigger/create', create_agent),
    path('agent-trigger/delete', delete_agent),

    path('company/<int:pk>', get_company),
    path('company/create', get_company_null),
    path('company-trigger/create', create_company),
    path('company-trigger/delete', delete_company),
]
