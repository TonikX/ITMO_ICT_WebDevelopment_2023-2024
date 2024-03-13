from rest_framework import serializers
from .models import *

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'full_name', 'passport_data', 'contact_data']

class NaturalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalPerson
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class LegalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalPerson
        fields = '__all__'

class NaturalPersonContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalPersonContract
        fields = '__all__'

class LegalPersonContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalPersonContract
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class InsuredEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuredEvent
        fields = '__all__'
        
class LegalPersonAndContractSerializer(serializers.ModelSerializer):
    contracts = LegalPersonContractSerializer(source='legalpersoncontract_set', many=True)

    class Meta:
        model = LegalPerson
        fields = ['id', 'full_name', 'contracts']
        read_only_fields = ['id', 'full_name', 'contracts']
