from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Skill, Warrior
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from .serializers import SkillSerializer, WarriorProfessionSerializer, WarriorSkillSerializer, SingleWarriorInfoSerializer, WarriorSerializer


class SkillListView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WarriorProfessionInfoView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorProfessionSerializer(warriors, many=True)
        return Response(serializer.data)


class WarriorSkillInfoView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSkillSerializer(warriors, many=True)
        return Response(serializer.data)


class SingleWarriorInfoView(RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = SingleWarriorInfoSerializer
    lookup_field = 'id'  # указываем поле, по которому будет производиться поиск


class WarriorDeleteView(DestroyAPIView):
    queryset = Warrior.objects.all()
    lookup_field = 'id'


class WarriorUpdateView(RetrieveUpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    lookup_field = 'id'
