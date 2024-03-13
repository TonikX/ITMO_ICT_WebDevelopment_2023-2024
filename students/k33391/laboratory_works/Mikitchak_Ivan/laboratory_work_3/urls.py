from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'natural-persons', NaturalPersonViewSet)
router.register(r'specializations', SpecializationViewSet)
router.register(r'legal-persons', LegalPersonViewSet)
router.register(r'natural-person-contracts', NaturalPersonContractViewSet)
router.register(r'legal-person-contracts', LegalPersonContractViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'insured-events', InsuredEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('same-agents-lps/<int:pk>/', SameAgentsLegalPersonsAPIView.as_view(), name='same_agents_lps'),
    path('agent-contracts-stats/<int:pk>/', AgentContractsStatsAPIView.as_view(), name='agent_contracts_stats'),
    path('insured-colleagues/<int:pk>/', InsuredColleaguesAPIView.as_view(), name='insured_colleagues'),
    path('insured-events-timeframe/', InsuredEventsTimeframeAPIView.as_view(), name='insured_events_timeframe'),
    path('lps-and-contracts/', LegalPersonsAndContractsAPIView.as_view(), name='lps_and_contracts'),
    path('report/', ReportAPIView.as_view(), name='report')
]