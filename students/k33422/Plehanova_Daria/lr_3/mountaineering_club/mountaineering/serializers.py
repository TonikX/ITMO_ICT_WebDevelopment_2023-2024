from rest_framework import serializers

from .models import Alpinist, Guide, Mountain, Route, Club


class AlpinistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alpinist
        fields = ['id', 'user_id', 'date_of_birth', 'address', 'level', 'club']
        read_only_fields = ['id']


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ['id', 'user_id', 'certification', 'years_of_experience']
        read_only_fields = ['id']


class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = ['id', 'name', 'height', 'country', 'region']
        read_only_fields = ['id']


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'mountain_id', 'name', 'difficulty', 'length', 'peak_height', 'estimated_time', 'description']
        read_only_fields = ['id']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'country', 'city', 'contact_person', 'email', 'phone', 'website', 'created_at']
        read_only_fields = ['id']
