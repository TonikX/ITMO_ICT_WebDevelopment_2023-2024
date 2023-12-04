from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserCreateView,
    DoctorViewSet, DoctorDetailViewSet,
    CabinetViewSet, CabinetDetailViewSet,
    PatientViewSet, PatientDetailViewSet,
    AppointmentViewSet, AppointmentDetailViewSet,
    PaymentViewSet, PaymentDetailViewSet,
    MedicalServiceViewSet, MedicalServiceDetailViewSet,
    ScheduleViewSet, ScheduleDetailViewSet
)
from djoser.views import TokenCreateView, TokenDestroyView, UserViewSet
import djoser
from rest_framework import routers


router = DefaultRouter()

router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'cabinets', CabinetViewSet, basename='cabinet')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'medical-services', MedicalServiceViewSet, basename='medicalservice')
router.register(r'schedules', ScheduleViewSet, basename='schedule')

urlpatterns = [
    path('', include(router.urls)),

    path('doctors/<int:pk>/', DoctorDetailViewSet.as_view(), name='doctor-detail'),
    path('cabinets/<int:pk>/', CabinetDetailViewSet.as_view(), name='cabinet-detail'),
    path('patients/<int:pk>/', PatientDetailViewSet.as_view(), name='patient-detail'),
    path('appointments/<int:pk>/', AppointmentDetailViewSet.as_view(), name='appointment-detail'),
    path('payments/<int:pk>/', PaymentDetailViewSet.as_view(), name='payment-detail'),
    path('medical-services/<int:pk>/', MedicalServiceDetailViewSet.as_view(), name='medicalservice-detail'),
    path('schedules/<int:pk>/', ScheduleDetailViewSet.as_view(), name='schedule-detail'),

    
]