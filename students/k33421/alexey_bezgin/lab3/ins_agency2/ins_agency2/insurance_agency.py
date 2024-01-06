from rest_framework import serializers

from models import *


class CompanyNotExpiredAgreementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
