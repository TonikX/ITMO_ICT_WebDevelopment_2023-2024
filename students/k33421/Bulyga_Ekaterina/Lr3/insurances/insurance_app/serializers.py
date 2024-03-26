from rest_framework import serializers
from .models import *
# from djoser.serializers import UserCreateSerializer
# from django.contrib.auth import get_user_model


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ['id', 'firstname', 'lastname', 'patronymic', 'passport', 'phone', 'address']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class InsureOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsureOrganization
        fields = '__all__'


class InsureAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsureAgent
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class InsuranceCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCase
        fields = '__all__'
