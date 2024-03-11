from rest_framework import serializers

from .models import *


class CompanyNotExpiredAgreementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AgentAgreementsCountSerializer(serializers.Serializer):
    # agent_name = serializers.CharField(source='agent__full_name')
    agent_name = serializers.CharField()
    collective_count = serializers.IntegerField()
    individual_count = serializers.IntegerField()


class UniqueEmployeesInCollectiveAgreementsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()


class CollectiveAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectiveAgreement
        fields = '__all__'


class IndividualAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualAgreement
        fields = '__all__'


class PayoutSummarySerializer(serializers.Serializer):
    collective_payout = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    individual_payout = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)


class CollectiveInsuranceClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectiveInsuranceClaim
        fields = '__all__'


class IndividualInsuranceClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualInsuranceClaim
        fields = '__all__'


class CompanyPayoutSummarySerializer(serializers.Serializer):
    bank_details = serializers.CharField(read_only=True)
    total_payout_first_category = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    total_payout_second_category = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    total_payout_third_category = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)


class AgentReportSerializer(serializers.Serializer):
    agent_id = serializers.IntegerField()
    agent_full_name = serializers.CharField()
    total_collective_agreements = serializers.IntegerField()
    total_collective_payout = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_individual_agreements = serializers.IntegerField()
    total_individual_payout = serializers.DecimalField(max_digits=10, decimal_places=2)

    total_collective_claims = serializers.IntegerField()
    total_collective_payout_claims = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_individual_claims = serializers.IntegerField()
    total_individual_payout_claims = serializers.DecimalField(max_digits=10, decimal_places=2)


class CompanyReportSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    company_full_name = serializers.CharField()
    total_collective_agreements = serializers.IntegerField()
    total_collective_payout = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_individual_agreements = serializers.IntegerField()
    total_individual_payout = serializers.DecimalField(max_digits=10, decimal_places=2)

    total_collective_claims = serializers.IntegerField()
    total_collective_payout_claims = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_individual_claims = serializers.IntegerField()
    total_individual_payout_claims = serializers.DecimalField(max_digits=10, decimal_places=2)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class AgentContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentContract
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

