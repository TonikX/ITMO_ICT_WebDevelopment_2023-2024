from django.shortcuts import render, get_object_or_404
from .models import Warrior, SkillOfWarrior, Skill
from .serializers import WarriorSerializer, ProfessionSerializer, SkillSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics


class WarriorList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDetail(
    generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response(
            {
                "Success": "Profession '{}' created succesfully.".format(
                    profession_saved.title
                )
            }
        )


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"skills": serializer.data})


class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response(
            {"Success": "Skill '{}' created succesfully.".format(skill_saved.title)}
        )
