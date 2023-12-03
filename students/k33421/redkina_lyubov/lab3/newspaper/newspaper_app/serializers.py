from rest_framework import serializers
from .models import Newspaper, PrintingHouse, PostOffice, NewspaperPrint, NewspaperArrival, NewspaperOrder, UserProfile
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = '__all__'

class PrintingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintingHouse
        fields = '__all__'

class PostOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostOffice
        fields = '__all__'

class NewspaperPrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewspaperPrint
        fields = '__all__'

class NewspaperArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewspaperArrival
        fields = '__all__'

class NewspaperOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewspaperOrder
        fields = '__all__'