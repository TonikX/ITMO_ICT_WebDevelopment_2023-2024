from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    role = serializers.CharField(source="get_role_display", read_only=True)

    class Meta:
        model = User
        fields = ["username", "role", "passport", "role", "salary", "employment_contract_id", "dismissal_agreement_id"]


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"


class CageSerializer(serializers.ModelSerializer):
    facility = FacilitySerializer()
    responsible = UserSerializer()

    class Meta:
        model = Cage
        fields = "__all__"

