from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActivityView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class FoodView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class DailyDataView(generics.ListCreateAPIView):
    queryset = DailyData.objects.all()
    serializer_class = DailyDataSerializer

class DailyDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyData.objects.all()
    serializer_class = DailyDataSerializer

class UserFoodView(generics.ListCreateAPIView):
    queryset = UserFood.objects.all()
    serializer_class = UserFoodSerializer

class UserFoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFood.objects.all()
    serializer_class = UserFoodSerializer
