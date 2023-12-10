from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer()
    hall = HallSerializer()

    class Meta:
        model = Copy
        fields = '__all__'


class CreateCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = '__all__'


class ReaderSerializer(serializers.ModelSerializer):
    hall = HallSerializer()
    education = serializers.CharField(source='get_education_display')

    class Meta:
        model = Reader
        fields = '__all__'


class CreateReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    copy = CopySerializer()
    reader = ReaderSerializer()

    class Meta:
        model = Assignment
        fields = '__all__'


class CreateAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
