from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Activity, Food, Profile, DailyData, UserFood

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

class DailyDataSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    activities = ActivitySerializer(many=True)

    class Meta:
        model = DailyData
        fields = '__all__'

class UserFoodSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    food = FoodSerializer()

    class Meta:
        model = UserFood
        fields = '__all__'
