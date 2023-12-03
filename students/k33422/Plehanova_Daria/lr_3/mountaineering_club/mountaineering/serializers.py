from rest_framework import serializers

from .models import Alpinist


class AlpinistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alpinist
        fields = ['id', 'date_of_birth', 'address', 'level', 'club']
        read_only_fields = ['id']
