from rest_framework import serializers

from .models import Alpinist, Guide


class AlpinistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alpinist
        fields = ['id', 'date_of_birth', 'address', 'level', 'club']
        read_only_fields = ['id']


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ['id', 'user_id', 'certification', 'years_of_experience']
        read_only_fields = ['id']
