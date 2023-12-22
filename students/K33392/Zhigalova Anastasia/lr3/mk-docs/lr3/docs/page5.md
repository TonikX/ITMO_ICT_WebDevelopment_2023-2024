# view.py

``` 
from rest_framework import viewsets, generics
from .models import Doctor, Cabinet, Patient, Appointment, Payment, MedicalService, Schedule
from .serializers import (
    DoctorSerializer, CabinetSerializer, PatientSerializer,
    AppointmentSerializer, PaymentSerializer, MedicalServiceSerializer, ScheduleSerializer
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class UserCreateView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('token_create')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer

class CabinetDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class MedicalServiceViewSet(viewsets.ModelViewSet):
    queryset = MedicalService.objects.all()
    serializer_class = MedicalServiceSerializer

class MedicalServiceDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalService.objects.all()
    serializer_class = MedicalServiceSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


``` 
