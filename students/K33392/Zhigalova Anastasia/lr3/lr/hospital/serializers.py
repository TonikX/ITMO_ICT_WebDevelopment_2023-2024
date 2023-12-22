from djoser.serializers import UserSerializer
from rest_framework import serializers
from djoser.serializers import TokenCreateSerializer

from .models import Doctor, Cabinet, Patient, Appointment, Payment, MedicalService, Schedule


class CustomTokenCreateSerializer(TokenCreateSerializer):

    def create(self, validated_data):
        token = super().create(validated_data)

        user = self.user
        token['user_id'] = user.id
        token['email'] = user.email

        return token


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'date_joined')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class MedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalService
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'