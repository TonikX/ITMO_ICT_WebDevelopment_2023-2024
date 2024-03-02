from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import WarriorSerializer, ProfessionSerializer, WarriorWithProfessionSerializer, WarriorWithSkillSerializer, RetriveWarriorSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView


class ListAPIWarior(ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ListAPIWariorWithProfession(ListAPIView):
    serializer_class = WarriorWithProfessionSerializer
    queryset = Warrior.objects.all()


class RetriveAPIWarriorwithSkillsAndProfession(RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ListAPIWariorWithSkill(ListAPIView):
    serializer_class = WarriorWithSkillSerializer
    queryset = Warrior.objects.all()


class DestroyAPIWarrior(DestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class UpdateAPIWarrior(UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):

    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})
