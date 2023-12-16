from rest_framework import serializers
from .models import Doctor, Patient, Service, Visit, Payment


class PaymentInfoSerializer(serializers.Serializer):
    payment_id = serializers.IntegerField(source='ID')
    date = serializers.DateField(source='Date')
    price = serializers.DecimalField(source='Price', max_digits=10, decimal_places=2)

    # Добавляем информацию о пациенте
    patient_name = serializers.CharField(source='ID_Visit.ID_Patient.Name')
    patient_surname = serializers.CharField(source='ID_Visit.ID_Patient.Surname')

    # Добавляем информацию о враче
    doctor_name = serializers.CharField(source='ID_Visit.ID_Doctor.Name')
    doctor_surname = serializers.CharField(source='ID_Visit.ID_Doctor.Surname')

    # Добавляем информацию об услуге
    service_name = serializers.CharField(source='ID_Visit.ID_Service.Name')
    service_description = serializers.CharField(source='ID_Visit.ID_Service.Description')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
