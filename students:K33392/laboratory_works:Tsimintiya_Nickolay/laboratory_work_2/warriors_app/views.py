from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Warrior
from .serialazer import WarriorSerialazer
# Create your views here.

class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerialazer(warriors, many=True)

        return Response({"Warriors": serializer.data})
