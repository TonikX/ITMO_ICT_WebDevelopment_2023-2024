from rest_framework import serializers


class UserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()