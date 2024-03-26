from django.urls import path
from .views import *


urlpatterns = [
    path('individual/', IndividualListCreateView.as_view(), name='individual-list-create'),
    path('individual/<int:pk>/', IndividualDetailView.as_view(), name='individual-detail'),

    path('type/', TypeListCreateView.as_view(), name='type-list-create'),
    path('type/<int:pk>/', TypeDetailView.as_view(), name='type-detail'),

    path('employee/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

    path('organization/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organization/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),

    path('insureorganization/', InsureOrganizationListCreateView.as_view(), name='insureorganization-list-create'),
    path('insureorganization/<int:pk>/', InsureOrganizationDetailView.as_view(), name='insureorganization-detail'),

    path('insureagent/', InsureAgentListCreateView.as_view(), name='insureagent-list-create'),
    path('insureagent/<int:pk>/', InsureAgentDetailView.as_view(), name='insureagent-detail'),

    path('contract/', ContractListCreateView.as_view(), name='contract-list-create'),
    path('contract/<int:pk>/', ContractDetailView.as_view(), name='contract-detail'),

    path('insurancecase/', InsuranceCaseListCreateView.as_view(), name='insurancecase-list-create'),
    path('insurancecase/<int:pk>/', InsuranceCaseDetailView.as_view(), name='insurancecase-detail'),
]
