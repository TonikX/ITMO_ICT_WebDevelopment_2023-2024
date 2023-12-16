from django.urls import path
from .views import (
    DoctorListView, DoctorDetailView,
    PatientListView, PatientDetailView,
    ServiceListView, ServiceDetailView,
    VisitListView, VisitDetailView,
    PaymentListView, PaymentDetailView, PaymentInfoView
)

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('visits/', VisitListView.as_view(), name='visit-list'),
    path('visits/<int:pk>/', VisitDetailView.as_view(), name='visit-detail'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('payment/<int:payment_id>/', PaymentInfoView.as_view(), name='payment_info'),
]
